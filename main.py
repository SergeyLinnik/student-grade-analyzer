def calculate_average(grades):
    """Возвращает средний балл по списку оценок"""
    return round(sum(grades) / len(grades), 2)


def classify_student(avg_score):
    """Возвращает статус студента: успешный или отстающий"""
    return "успешный" if avg_score >= 75 else "отстающий"


def print_student_info(student):
    """Выводит информацию о студенте в форматированном виде"""
    avg = calculate_average(student['grades'])
    status = classify_student(avg)
    print(f"Имя: {student['name']}")
    print(f"Средний балл: {avg}")
    print(f"Статус: {status}\n")


def print_all_students(students_list):
    """Выводит информацию обо всех студентах"""
    print("=== Информация о студентах ===\n")
    for student in students_list:
        print_student_info(student)


def calculate_total_average(students_list):
    """Вычисляет общий средний балл по всем студентам"""
    return round(sum(calculate_average(student['grades']) for student in students_list) / len(students_list), 2)


def add_student(students_list, name, grades):
    """Добавляет нового студента в список"""
    new_student = {"name": name, "grades": grades}
    students_list.append(new_student)
    print(f"Студент '{name}' добавлен.\n")
    return new_student


def remove_lowest_performing_student(students_list):
    """Удаляет студента с самым низким средним баллом"""
    if not students_list:
        print("Список студентов пуст. Нечего удалять.")
        return

    min_student = min(students_list, key=lambda s: calculate_average(s["grades"]))
    students_list.remove(min_student)
    print(f"Студент '{min_student['name']}' с наименьшим средним баллом удалён из списка.\n")


# === Тело программы ===

# Список студентов
students = [
    {"name": "Алексей", "grades": [80, 90, 75, 85]},
    {"name": "Мария", "grades": [60, 70, 65, 58]},
    {"name": "Иван", "grades": [92, 88, 95, 90]},
    {"name": "Ольга", "grades": [50, 55, 60, 48]}
]

# Вывод начального списка
print_all_students(students)

# Вывод общего среднего балла
total_avg = calculate_total_average(students)
print(f"Общий средний балл по всем студентам: {total_avg}\n")

# Добавляем нового студента
add_student(students, "Дмитрий", [70, 75, 80, 78])

# Пересчитываем общий средний балл после добавления
total_avg = calculate_total_average(students)
print(f"Новый общий средний балл: {total_avg}\n")

# Удаляем студента с самым низким баллом
remove_lowest_performing_student(students)

# Пересчитываем и выводим финальные данные
total_avg = calculate_total_average(students)
print(f"Финальный общий средний балл: {total_avg}\n")

# Вывод финального списка студентов
print_all_students(students)
