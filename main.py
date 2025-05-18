def calculate_average(grades):
    """Возвращает средний балл по списку оценок. Проверяет входные данные."""
    if not isinstance(grades, (list, tuple)):
        print("Ошибка: Оценки должны быть списком или кортежем.")
        return 0

    if len(grades) == 0:
        print("Ошибка: Список оценок пуст.")
        return 0

    try:
        average = sum(grades) / len(grades)
        return round(average, 2)
    except TypeError:
        print("Ошибка: Все оценки должны быть числами.")
        return 0


def classify_student(avg_score):
    """Возвращает статус студента: успешный или отстающий"""
    if avg_score is None or not isinstance(avg_score, (int, float)):
        return "не определён"
    return "успешный" if avg_score >= 75 else "отстающий"


def print_student_info(student):
    """Выводит информацию о студенте в форматированном виде"""
    if not isinstance(student, dict):
        print("Ошибка: Неверный формат данных студента.\n")
        return

    name = student.get('name')
    grades = student.get('grades')

    if not isinstance(name, str) or not isinstance(grades, list):
        print(f"Ошибка: Некорректные данные для студента {name}.\n")
        return

    avg = calculate_average(grades)
    status = classify_student(avg)

    print(f"Имя: {name}")
    print(f"Средний балл: {avg}")
    print(f"Статус: {status}\n")


def print_all_students(students_list):
    """Выводит информацию обо всех студентах"""
    if not isinstance(students_list, list):
        print("Ошибка: Список студентов должен быть типом 'list'.\n")
        return

    print("=== Информация о студентах ===\n")
    for student in students_list:
        print_student_info(student)


def calculate_total_average(students_list):
    """Вычисляет общий средний балл по всем студентам"""
    if not isinstance(students_list, list):
        print("Ошибка: Список студентов должен быть типом 'list'.")
        return 0

    if len(students_list) == 0:
        print("Список студентов пуст.")
        return 0

    total_avg_sum = 0
    count = 0

    for student in students_list:
        if not isinstance(student, dict) or 'grades' not in student:
            continue
        avg = calculate_average(student['grades'])
        if avg is not None:
            total_avg_sum += avg
            count += 1

    if count == 0:
        print("Нет допустимых студентов для расчёта общего среднего балла.")
        return 0

    return round(total_avg_sum / count, 2)


def add_student(students_list, name, grades):
    """Добавляет нового студента в список"""
    if not isinstance(students_list, list):
        print("Ошибка: Список студентов должен быть типом 'list'.")
        return None

    if not isinstance(name, str):
        print("Ошибка: Имя студента должно быть строкой.")
        return None

    if not isinstance(grades, list):
        print("Ошибка: Оценки должны быть списком.")
        return None

    new_student = {"name": name, "grades": grades}
    students_list.append(new_student)
    print(f"Студент '{name}' добавлен.\n")
    return new_student


def remove_lowest_performing_student(students_list):
    """Удаляет студента с самым низким средним баллом"""
    if not isinstance(students_list, list):
        print("Ошибка: Список студентов должен быть типом 'list'.")
        return

    if not students_list:
        print("Список студентов пуст. Нечего удалять.")
        return

    # Вычисляем средние баллы
    students_with_avg = []
    for student in students_list:
        if not isinstance(student, dict) or 'grades' not in student:
            continue
        avg = calculate_average(student['grades'])
        if avg is not None:
            students_with_avg.append({**student, "average": avg})

    if not students_with_avg:
        print("Нет допустимых студентов для удаления.")
        return

    min_student = min(students_with_avg, key=lambda s: s["average"])
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
