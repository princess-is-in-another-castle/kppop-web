from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt',  'created_date')


admin.site.register(Article, ArticleAdmin)