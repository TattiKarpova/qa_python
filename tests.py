import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Алгоритмы')
        collector.set_book_genre('Алгоритмы', "Ужасы")
        collector.add_book_in_favorites('Алгоритмы')
        assert 'Алгоритмы' in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', "Мультфильмы")
        collector.add_book_in_favorites('Маленький принц')
        collector.delete_book_from_favorites('Маленький принц')
        assert 'Маленький принц' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('My Book')
        collector.set_book_genre('My Book', 'Ужасы')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Детектив')
        collector.add_book_in_favorites('My Book')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['My Book', '1984']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Том Сойер')
        collector.set_book_genre('Том Сойер', 'Мультфильмы')
        collector.add_new_book('Техасская резня бензопилой')
        collector.set_book_genre('Техасская резня бензопилой', 'Ужасы')
        assert collector.get_books_for_children() == ['Том Сойер']

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мир Российского футбола')
        collector.set_book_genre('Мир Российского футбола', 'Комедии')
        collector.add_new_book('Гарри Поттер и Могучий рыцарь')
        collector.set_book_genre('Гарри Поттер и Могучий рыцарь', 'Ужасы')
        collector.add_new_book('Цунами')
        collector.set_book_genre('Цунами','Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == ['Мир Российского футбола']
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гарри Поттер и Могучий рыцарь','Цунами']

    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Граф Монте Кристо')
        collector.add_new_book('Граф Монте Кристо')  # Добавляем повторно
        assert len(collector.books_genre) == 1

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Могучий рыцарь')
        collector.set_book_genre('Гарри Поттер и Могучий рыцарь', 'Ужасы')
        assert collector.get_book_genre('Гарри Поттер и Могучий рыцарь') == 'Ужасы'

    def test_delete_book_from_favorites_notexist_book(self):
        collector = BooksCollector()
        collector.add_new_book('Принц Персии')
        collector.set_book_genre('Принц Персии', 'Фантастика')
        collector.add_book_in_favorites('Принц Персии')
        collector.delete_book_from_favorites('Левая книга')  # Попытка удалить несуществующую книгу
        assert len(collector.favorites) == 1

@pytest.mark.parametrize('book_name, genre',[
    ('Тишина', 'Ужасы'),
    ('Дельфин', 'Фантастика'),
    ('Дверь', 'Мультфильмы')])
def test_set_book_genre(book_name, genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre
