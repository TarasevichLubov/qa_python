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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_book_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book('Приключения Буратино')
        result = collector.get_books_genre()
        assert 'Приключения Буратино' in result

    def test_add_new_book_genre_miss(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Буратино')
        assert collector.get_book_genre('Приключения Буратино') == ''

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Мастер и маргарита', 'Фантастика'],
            ['Дракула', 'Ужасы'],
            ['Десять негритят', 'Детективы'],
            ['Приключения Буратино', 'Мультфильмы'],
            ['Трое в лодке', 'Комедии']
        ]
    )
    def test_get_book_genre_check_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_add_new_book_double_add_block(self):
        collector = BooksCollector()
        collector.add_new_book('Кладбище домашних животных')
        collector.add_new_book('Кладбище домашних животных')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['Я', 'Евгений Онегин. Поэмы. Драмы. Сказки ч.1'])
    def test_add_new_book_name_length_1_or_40_true(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['Клуб любителей книг и пирогов из картофел', ''])
    def test_add_new_book_name_length_0_or_41_false(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_get_books_with_specific_genre_check_horror_books(self):
        collector = BooksCollector()
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        collector.add_new_book('Мастер и маргарита')
        collector.set_book_genre('Мастер и маргарита', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Кладбище домашних животных']

    def test_books_for_children_correct_list_book_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        collector.add_new_book('Приключения Буратино')
        collector.set_book_genre('Приключения Буратино', 'Мультфильмы')
        assert ('Кладбище домашних животных' not in collector.get_books_for_children())

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Буратино')
        collector.add_book_in_favorites('Приключения Буратино')
        assert ('Приключения Буратино' in collector.get_list_of_favorites_books())

    def test_add_book_in_favorites_list_double_add_block(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Буратино')
        collector.add_book_in_favorites('Приключения Буратино')
        collector.add_book_in_favorites('Приключения Буратино')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_check_del_book(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')
        collector.delete_book_from_favorites('Десять негритят')
        assert 'Десять негритят' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_check_del_not_all_book(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')
        collector.add_new_book('Приключения Буратино')
        collector.add_book_in_favorites('Приключения Буратино')
        collector.delete_book_from_favorites('Десять негритят')
        assert len(collector.get_list_of_favorites_books()) == 1
