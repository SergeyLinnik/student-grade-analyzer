def calculate_average(grades):
    """Возвращает средний балл по списку оценок. Защищает от деления на 0."""
    try:
        if not grades:
            raise ValueError("Список оценок пуст.")
        return round(sum(grades) / len(grades), 2)
    except ZeroDivisionError:
        print("Ошибка: список оценок не должен быть пустым.")
        return 0
    except Exception as e:
        print(f"Ошибка при подсчёте среднего балла: {e}")
        return 0


def classify_student(avg_score):
    """Возвращает статус студента: успешный или отстающий"""
    return "успешный" if avg_score >= 75 else "отстающий"


def print_student_info(student):
    """Выводит информацию о студенте в форматированном виде"""
    try:
        if not isinstance(student, dict) or 'grades' not in student or 'name' not in student:
            raise ValueError("Некорректные данные о студенте")
        avg = calculate_average(student['grades'])
        status = classify_student(avg)
        print(f"Имя: {student['name']}")
        print(f"Средний балл: {avg}")
        print(f"Статус: {status}\n")
    except Exception as e:
        print(f"Ошибка при выводе информации о студенте: {e}")


def print_all_students(students_list):
    """Выводит информацию обо всех студентах"""
    try:
        if not students_list:
            print("Список студентов пуст.\n")
            return

        print("=== Информация о студентах ===\n")
        for student in students_list:
            print_student_info(student)
    except Exception as e:
        print(f"Ошибка при выводе списка студентов: {e}")


def calculate_total_average(students_list):
    """Вычисляет общий средний балл по всем студентам"""
    try:
        if not students_list:
            raise ValueError("Список студентов пуст.")

        total_avg = sum(calculate_average(student['grades']) for student in students_list)
        return round(total_avg / len(students_list), 2)
    except Exception as e:
        print(f"Ошибка при расчёте общего среднего балла: {e}")
        return 0


def add_student(students_list, name, grades):
    """Добавляет нового студента в список"""
    try:
        if not isinstance(name, str) or not isinstance(grades, list):
            raise ValueError("Некорректные данные при добавлении студента.")
        new_student = {"name": name, "grades": grades}
        students_list.append(new_student)
        print(f"Студент '{name}' добавлен.\n")
        return new_student
    except Exception as e:
        print(f"Ошибка при добавлении студента: {e}")
        return None


def remove_lowest_performing_student(students_list):
    """Удаляет студента с самым низким средним баллом"""
    try:
        if not students_list:
            print("Список студентов пуст. Нечего удалять.")
            return

        min_student = min(students_list, key=lambda s: calculate_average(s["grades"]))
        students_list.remove(min_student)
        print(f"Студент '{min_student['name']}' с наименьшим средним баллом удалён из списка.\n")
    except Exception as e:
        print(f"Ошибка при удалении студента: {e}")


# === Тело программы ===

# Список студентов
students = [
    {"name": "Алексей", "grades": [80, 90, 75, 85]},
    {"name": "Мария", "grades": [60, 70, 65, 58]},
    {"name": "Иван", "grades": [92,
