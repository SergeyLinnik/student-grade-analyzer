# Словарь library: ключ — название книги, значение — словарь с информацией о книге
library = {}

def add_book(title, author, year):
    """
    Добавляет или обновляет информацию о книге в библиотеке.
    
    :param title: Название книги
    :param author: Автор книги
    :param year: Год издания
    """
    if title in library:
        print(f"Книга '{title}' уже существует в библиотеке. Хотите обновить информацию?")
        choice = input("Введите 'да' для обновления, любую другую клавишу для отмены: ").strip().lower()
        if choice == 'да':
            library[title] = {
                "author": author,
                "year": year,
                "available": None  # Не определено при добавлении
            }
            print(f"Информация о книге '{title}' успешно обновлена.\n")
    else:
        library[title] = {
            "author": author,
            "year": year,
            "available": True  # По умолчанию книга доступна
        }
        print(f"Книга '{title}' успешно добавлена в библиотеку.\n")


def remove_book(title):
    """
    Удаляет книгу из библиотеки по её названию.
    
    :param title: Название книги
    """
    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена из библиотеки.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")


def issue_book(title):
    """
    Отмечает книгу как выданную (available = False).
    
    :param title: Название книги
    """
    if title in library:
        if library[title]["available"]:
            library[title]["available"] = False
            print(f"Книга '{title}' успешно выдана.\n")
        else:
            print(f"Книга '{title}' уже выдана.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")


def return_book(title):
    """
    Отмечает книгу как возвращённую (available = True).
    
    :param title: Название книги
    """
    if title in library:
        if not library[title]["available"]:
            library[title]["available"] = True
            print(f"Книга '{title}' успешно возвращена в библиотеку.\n")
        else:
            print(f"Книга '{title}' уже находится в библиотеке.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")


def book_list_view(library):
    """
    Выводит список всех книг в библиотеке
