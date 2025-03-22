from main import BooksCollector
import pytest

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
        # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_without_genre_success_added(self, collector):
        collector.add_new_book('Чужак')
        assert 'Чужак' in collector.get_books_genre()
        assert collector.books_genre['Чужак'] == ''

    @pytest.mark.parametrize('book_names_dif_len, name_len',
                            [('Я', 1),
                            ('Как научуиться программировать на Python', 40)])
    def test_add_new_book_1_40_valid_boundary_values_success_added(self, collector, book_names_dif_len, name_len):

        collector.add_new_book(book_names_dif_len)
        assert book_names_dif_len in collector.books_genre
        assert len(book_names_dif_len) == name_len

    @pytest.mark.parametrize('book_names_dif_len, name_len',
                            [('', 0),
                            ('Программирование на Python от нуля до проф', 42)])
    def test_add_new_book_not_valid_boundary_values_0_42_not_added(self, collector, book_names_dif_len, name_len):

        collector.add_new_book(book_names_dif_len)
        assert book_names_dif_len not in collector.books_genre
        assert len(book_names_dif_len) == name_len

    @pytest.mark.parametrize('book_names_with_spec_or_nums',
                            ['Метро 2033', '1984', '22.11/63']
                             )
    def test_add_new_book_contains_special_chars_or_nums_added(self, collector, book_names_with_spec_or_nums):

        collector.add_new_book(book_names_with_spec_or_nums)
        assert book_names_with_spec_or_nums in collector.books_genre

    def test_set_book_genre_available_in_list_added(self, collector):

        collector.add_new_book('Вокруг света за 80 дней')
        collector.set_book_genre('Вокруг света за 80 дней', 'Фантастика')
        assert 'Вокруг света за 80 дней' in collector.books_genre and collector.books_genre['Вокруг света за 80 дней'] == 'Фантастика'

    def test_set_book_genre_not_available_in_list_not_added(self, collector):

        collector.add_new_book('Джейн Эйр')
        collector.set_book_genre('Джейн Эйр', 'Роман')
        assert 'Роман' not in collector.genre
        assert collector.books_genre['Джейн Эйр'] == ''

    def test_get_book_genre_available_in_list_shows(self, collector):

        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.set_book_genre('Мечтают ли андроиды об электроовцах?', 'Фантастика')
        assert collector.get_book_genre('Мечтают ли андроиды об электроовцах?') == 'Фантастика'

    def test_get_book_genre_for_book_without_genre_dont_show(self, collector):

        collector.add_new_book('Левая рука тьмы')
        assert collector.get_book_genre('Левая рука тьмы') == ''

    def test_get_book_genre_without_book_dont_show(self, collector):

        assert None == collector.get_book_genre('Пикник на обочине')

    def test_get_books_with_specific_genre_available_in_list_show(self, collector):

        collector.add_new_book('Нейромант')
        collector.set_book_genre('Нейромант', 'Фантастика')
        assert 'Нейромант' in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_with_specific_genre_without_genre_dont_show(self, collector):

        collector.add_new_book('Игра Эндера')
        assert 'Игра Эндера' not in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_with_specific_genre_without_book_dont_show(self, collector):

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 0

    def test_get_books_for_children_available_in_list_for_children_show_success(self, collector):

        collector.add_new_book('Видоизменённый углерод')
        collector.set_book_genre('Видоизменённый углерод', 'Фантастика')
        assert 'Видоизменённый углерод' in collector.get_books_for_children()

    def test_get_books_for_children_available_not_in_list_for_children_dont_show(self, collector):

        collector.add_new_book('Коллекционер')
        collector.set_book_genre('Коллекционер', 'Ужасы')
        assert len(collector.get_books_for_children()) == 0

    def test_get_books_for_children_not_available_without_genre_dont_show(self, collector):

        collector.add_new_book('Дракула')
        assert len(collector.get_books_for_children()) == 0

    def test_get_books_for_children_1_for_children_2_not_show_only_available(self, collector):

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.add_new_book('Задача трёх тел')
        collector.set_book_genre('Задача трёх тел', 'Фантастика')
        result = collector.get_books_for_children()
        assert 'Задача трёх тел' in result
        assert 'Дракула' not in result

    def test_add_book_in_favorites_list_success_added(self, collector):

        collector.add_new_book('Гиперион')
        collector.add_book_in_favorites('Гиперион')
        assert 'Гиперион' in collector.favorites

    def test_add_book_in_favorites_list_without_book_not_found(self, collector):

        collector.add_book_in_favorites('Гиперион')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_success_deleted(self, collector):

        collector.add_new_book('Квантовый вор')
        collector.set_book_genre('Квантовый вор', 'Фантастика')
        collector.add_book_in_favorites('Квантовый вор')
        assert 'Квантовый вор' in collector.favorites
        collector.delete_book_from_favorites('Квантовый вор')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_without_favorite_book_not_success(self, collector):

        collector.add_new_book('Террор')
        collector.delete_book_from_favorites('Террор')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_without_book_not_success(self, collector):

        collector.delete_book_from_favorites('Ребёнок Розмари')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_success_show(self, collector):

        collector.add_new_book('Пробуждение Левиафана')
        collector.set_book_genre('Пробуждение Левиафана', 'Фантастика')
        collector.add_book_in_favorites('Пробуждение Левиафана')
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.add_book_in_favorites('Марсианин')
        assert 'Марсианин' in collector.favorites and 'Пробуждение Левиафана' in collector.favorites
        assert len(collector.favorites) == 2

    def test_get_list_of_favorites_books_without_genre_success_show(self, collector):

        collector.add_new_book('Отказ всех систем')
        collector.add_book_in_favorites('Отказ всех систем')
        collector.add_new_book('Пространство Откровения')
        collector.add_book_in_favorites('Пространство Откровения')
        assert 'Пространство Откровения' in collector.favorites and 'Отказ всех систем' in collector.favorites
        assert len(collector.favorites) == 2

    def test_get_list_of_favorites_books_without_favorite_books_dont_show(self, collector):

        collector.add_new_book('Призрак дома на холме')
        collector.add_new_book('Колыбельная')
        assert 'Призрак дома на холме' in collector.books_genre and 'Колыбельная' in collector.books_genre
        assert 'Колыбельная' not in collector.favorites and 'Призрак дома на холме' not in collector.favorites
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_without_books_dont_show(self, collector):

        collector.get_list_of_favorites_books()
        assert len(collector.favorites) == 0