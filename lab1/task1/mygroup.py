from lab1.task1.generate_list_of_students import *


def get_and_print_above_average_students(grade_average, students):
    students_exists = False
    # checks if there is at least one student with a higher grade average
    for student in students:
        if sum(student["marks"]) / len(student["marks"]) > grade_average:
            students_exists = True
            break

    if not (2.0 <= grade_average <= 5.0):
        print("Грррр, неправильные данные, вырубаю программу")
        return
    if students_exists:
        print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(40), "Оценки".ljust(20))

        for student in students:
            if sum(student["marks"]) / len(student["marks"]) > grade_average:
                print(student["name"].ljust(15), student["surname"].ljust(15), str(student["exams"]).ljust(40),
                      str(student["marks"]).ljust(20))
    else:
        print("Таких студентов нету.")


# main program starts here
grade_average = float(input("Введите средний балл(от 2.0 до 5.0): "))
groupmates = int(input("Введите количество студентов для генерации списка: "))
if groupmates <= 0:
    print("\nСтудентов не может не быть, поэтому пусть будет 404 человека\n")
    groupmates = generate_list(404)
else:
    groupmates = generate_list(groupmates)

get_and_print_above_average_students(grade_average, groupmates)
