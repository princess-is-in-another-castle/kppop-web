from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login


# Create your views here.
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        # Здесь будет основной код представления
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if not is_title_unique(form["title"]):
                form['errors'] = u"Название статьи не уникально"
                return render(request, 'create_post.html', {'form': form})
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"] and is_title_unique(form["title"]):
                # если поля заполнены без ошибок
                Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect("archive")
            # перейти на страницу со всеми статьями
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404


def is_title_unique(title):
    posts = Article.objects.all()
    for post in posts:
        if title == post.title:
            return False


def create_user(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'login': request.POST["login"], 'psw': request.POST["psw"]
        }
        if not is_login_exists(form['login']):
            form['errors'] = u"Пользователь с таким именем уже существует"
            return render(request, 'create_user.html', {'form': form})

        # в словаре form будет храниться информация, введенная пользователем
        if form["login"] and form["psw"]:
            User.objects.create_user(username=form["login"], password=form["psw"])
            # если поля заполнены без ошибок
        else:
            # если введенные данные некорректны
            form['errors'] = u"Некорректные данные"
            return render(request, 'create_user.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'create_user.html', {})


def is_login_exists(username):
    try:
        User.objects.get(username=username)
        print("Пользователь с таким именем уже есть")
        return False
        # если пользователь существует, то ошибки не произойдет и программа
        # удачно доберется до следующей строчки
    except User.DoesNotExist:
        print("Этот логин свободен")
        return True


def auth_user(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'login': request.POST["login"], 'psw': request.POST["psw"]
        }
        user = authenticate(username=form['login'], password=form["psw"])
        if user is None:
            form['errors'] = u"Этого аккаунта не существует"
            return render(request, 'auth_user.html', {'form': form})

        login(request, user)
        form['success'] = u"Авторизация прошла успешно"
        return render(request, 'auth_user.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'auth_user.html', {})
