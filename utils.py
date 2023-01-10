import json

from json import JSONDecodeError

from constants import JSON_FILE, JSON_COMMENTS


class PostHandler:
    @staticmethod
    def get_posts_all():
        """
        Метод возвращает все посты, и обрабатывает исключение JSONDecodeError.
        :return: все посты из json формата в формате python.
        """
        posts = []
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                posts = json.load(f)
        except FileNotFoundError:
            print('Ошибка файл не найден')
            return posts
        except JSONDecodeError:
            print('Ошибка получения данных из Json')
            return posts
        return posts

    def get_posts_by_user(self, user_name):
        """
        Метод возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError`
        если такого пользователя нет и пустой список, если у пользователя нет постов.
        :param user_name: атрибут метода для поиска поста по имени.
        :return: посты определенного пользователя.
        """
        posts = []
        posts_data = self.get_posts_all()
        try:
            for poster in posts_data:
                if user_name.lower() == poster['poster_name'].lower():
                    posts.append(poster)
        except ValueError:
            print('Такого пользователя нет')
            return posts
        return posts

    @staticmethod
    def get_comments_by_post_id(post_id):
        """
        Метод возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError`
        если такого поста нет и пустой список, если у поста нет комментов.
        :param post_id: атрибут метода для поиска поста, является идентификационный номер поста.
        :return: комментарий по id поста.
        """
        data_comments = []
        try:
            with open(JSON_COMMENTS, 'r', encoding='utf-8') as f:
                data_comments = json.load(f)
        except FileNotFoundError:
            print('Ошибка файл не найден')
        except JSONDecodeError:
            print('Ошибка получения данных из Json')

        comments = []
        try:
            for comment in data_comments:
                if post_id == comment['post_id']:
                    comments.append(comment)
        except ValueError:
            print('Такого поста нет')
            return comments
        return comments

    def search_for_posts(self, query):
        """
        Метод возвращает список постов по ключевому слову.
        :param query: введенное ключевое слово.
        :return: список постов в котором есть введенное ключевое слово.
        """
        posts = []
        posts_data = self.get_posts_all()
        try:
            for post in posts_data:
                if query.lower() in post['content'].lower():
                    posts.append(post)
        except ValueError:
            print('Такого ключевого слова в постах нет')
            return posts
        return posts

    def get_post_by_pk(self, pk):
        """
        Метод возвращает один пост по его идентификатору.
        :param pk: идентификатор для поиска поста.
        :return: пост.
        """
        posts_data = self.get_posts_all()
        post_pk = []
        try:
            for post in posts_data:
                if pk == post['pk']:
                    post_pk.append(post)
        except ValueError:
            print('Поста по такому "pk" нет')
            return post_pk
        return post_pk


post_handler = PostHandler()
print(post_handler.get_post_by_pk(1))
