# Список студентов. Каждый студент — словарь с 'name' и 'grades'
students = [
    {"name": "Алексей", "grades": [80, 90, 75, 85]},
    {"name": "Мария", "grades": [60, 70, 65, 58]},
    {"name": "Иван", "grades": [92, 88, 95, 90]},
    {"name": "Ольга", "grades": [50, 55, 60, 48]}
]


def calculate_average(grades):
    """Возвращает средний балл по списку оценок"""
    return round(sum(grades) / len(grades), 2)


def calculate_total_average(students_list):
    """Вычисляет общий средний балл по всем студентам"""
    total_sum = sum(calculate_average(student['grades']) for student in students_list)
    return round(total_sum / len(students_list), 2)


def classify_student(avg_score):
    """Возвращает статус студента: успешный или отстающий"""
    return "успешный" if avg_score >= 75 else "отстающий"


# 2-4. Вычисляем и выводим информацию о каждом студенте
print("=== Информация о студентах ===\n")
for student in students:
    avg = calculate_average(student['grades'])
    status = classify_student(avg)
    print(f"Имя: {student['name']}")
    print(f"Средний балл: {avg}")
    print(f"Статус: {status}\n")


# 5. Общий средний балл
total_avg = calculate_total_average(students)
print(f"Общий средний балл по всем студентам: {total_avg}\n")


# 6. Добавляем нового студента
new_student = {"name": "Дмитрий", "grades": [70, 75, 80, 78]}
students.append(new_student)
print(f"Студент '{new_student['name']}' добавлен.\n")


# Пересчитываем общий средний балл после добавления
total_avg = calculate_total_average(students)
print(f"Новый общий средний балл: {total_avg}\n")


# 7. Удаляем студента с самым низким средним баллом
students_with_avg = [
    {"name": s["name"], "grades": s["grades"], "average": calculate_average(s["grades"])} 
    for s in students
]

# Находим студента с минимальным средним баллом
min_student = min(students_with_avg, key=lambda x: x["average"])
students = [s for s in students if s["name"] != min_student["name"]]
print(f"Студент '{min_student['name']}' с наименьшим средним баллом удалён из списка.\n")


# Пересчитываем общий средний балл после удаления
total_avg = calculate_total_average(students)
print(f"Финальный общий средний балл: {total_avg}\n")


# Вывод финального списка студентов
print("=== Финальный список студентов ===\n")
for student in students:
    avg = calculate_average(student['grades'])
    status = classify_student(avg)
    print(f"Имя: {student['name']}")
    print(f"Средний балл: {avg}")
    print(f"Статус: {status}\n")
