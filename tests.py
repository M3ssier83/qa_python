import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

@pytest.mark.parametrize("book_name, expected_count", [
    ("Мастера и Маргарита", 1),
    ("Приключения капитана Врунгеля в океане чудес", 1),
    ("", 0),
    ("А", 1),
    ("Би", 1),
    ("Тайны старого замка: загадка исчезнувших", 1),
    ("Путеводитель по мирам: путешествие через вселенные", 0),
    ("Как стать мастером программирования за 30 дней без усилий", 0),
])
def test_add_new_book(book_name, expected_count):
    collector = BooksCollector()
    collector.add_new_book(book_name.strip())
    assert len(collector.get_books_genre()) == expected_count

@pytest.mark.parametrize("book_name, genre, expected_genre", [
    ("Тринадцатая сказка", "Фантастика", "Фантастика"),
    ("Несуществующая книга", "Ужасы", None),
    ("Тринадцатая сказка", "Роман", None),
    ("Тринадцатая сказка", "", None),
])
def test_set_book_genre(book_name, genre, expected_genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == expected_genre

@pytest.mark.parametrize("book_name, genre", [
    ("1984", "Фантастика"),
    ("Оно", "Ужасы"),
    ("Убийство в Восточном экспрессе", "Детективы"),
    ("Земляне", "Фантастика"),
    ("Тайна третьей планеты", "Мультфильмы"),
    ("Несуществующая книга", None),
])
def test_get_book_genre(book_name, genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre

@pytest.mark.parametrize("books, genre, expected_books", [
    ([("Падение Гипериона", "Фантастика"), ("Проклятая усадьба", "Ужасы")], "Фантастика", ["Падение Гипериона"]),
    ([("Стеклянный город", "Фантастика"), ("Падение Гипериона", "Фантастика")], "Фантастика", ["Стеклянный город", "Падение Гипериона"]),
    ([("Танец с демонами", "Детективы")], "Комедии", []),
    ([("Книга без жанра", "")], "Фантастика", []),
])
def test_get_books_with_specific_genre(books, genre, expected_books):
    collector = BooksCollector()
    for name, book_genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, book_genre)
    assert collector.get_books_with_specific_genre(genre) == expected_books

@pytest.mark.parametrize("books, expected_books", [
    ([("Остров теней", "Фантастика"), ("Лабиринт страха", "Ужасы")], ["Остров теней"]),
    ([("Солнечный экспресс", "Мультфильмы")], ["Солнечный экспресс"]),
    ([("Легенды ночи", "Ужасы")], []),
    ([("Фантастика для детей", "Фантастика"), ("Ужасы для взрослых", "Ужасы")], ["Фантастика для детей"]),
])
def test_get_books_for_children(books, expected_books):
    collector = BooksCollector()
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    assert collector.get_books_for_children() == expected_books

@pytest.mark.parametrize("book_name, expected_favorites", [
    ("Земля призраков", ["Земля призраков"]),
    ("Несуществующая книга", []),
    ("Земля призраков", ["Земля призраков"]),
])
def test_add_book_in_favorites(book_name, expected_favorites):
    collector = BooksCollector()
    collector.add_new_book("Земля призраков")
    collector.add_book_in_favorites(book_name)
    collector.add_book_in_favorites(book_name)
    assert collector.get_list_of_favorites_books() == expected_favorites

@pytest.mark.parametrize("initial_books, book_to_delete, expected_favorites", [
    (["Тайны древних", "Кодекс Судьбы"], "Кодекс Судьбы", ["Тайны древних"]),
    (["Тайны древних"], "Затерянный храм", ["Тайны древних"]),
    (["Книга в избранном"], "Книга в избранном", []),
])
def test_delete_book_from_favorites(initial_books, book_to_delete, expected_favorites):
    collector = BooksCollector()
    for book in initial_books:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
    collector.delete_book_from_favorites(book_to_delete)
    assert collector.get_list_of_favorites_books() == expected_favorites

@pytest.mark.parametrize("books, expected_favorites", [
    (["Секрет вечности", "Хранитель тайн"], ["Секрет вечности", "Хранитель тайн"]),
    ([], []),
    (["Книга удаленная"], []),
])
def test_get_list_of_favorites_books(books, expected_favorites):
    collector = BooksCollector()
    for book in books:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
    for book in books:
        collector.delete_book_from_favorites(book)
    assert collector.get_list_of_favorites_books() == expected_favorites
