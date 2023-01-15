import json

from json import JSONDecodeError

from constants import JSON_POSTS, JSON_COMMENTS


class PostHandler:

    @staticmethod
    def load_json_file(filename):
        """
        Метод читает файл JSON и обрабатывает его исключения.
        :param filename: JSON файл.
        :return: список из файла JSON.
        """
        data = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print('Ошибка файл не найден')
        except JSONDecodeError:
            print('Ошибка получения данных из Json')
        return data

    def get_posts_all(self):
        """
        Метод возвращает все посты из файла posts.json.
        :return: все посты из json формата в формате python.
        """
        posts_data = self.load_json_file(JSON_POSTS)
        return posts_data

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

    def get_comments_by_post_id(self, post_id):
        """
        Метод возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError`
        если такого поста нет и пустой список, если у поста нет комментов.
        :param post_id: атрибут метода для поиска поста, является идентификационный номер поста.
        :return: комментарий по id поста.
        """
        found_posts = self.get_post_by_pk(post_id)
        if not found_posts:
            raise ValueError('Такого поста нет')

        comments = []
        data_comments = self.load_json_file(JSON_COMMENTS)
        try:
            for comment in data_comments:
                if post_id == comment['post_id']:
                    comments.append(comment)
        except KeyError:
            print('Комментария по такому ключу нет')
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
                    # post['content'] = post['content'][0:50] + '...'
                    posts.append(post)
        except ValueError:
            print('Такого ключевого слова в постах нет')
        return posts

    def get_post_by_pk(self, pk):
        """
        Метод возвращает один пост по его идентификатору.
        :param pk: идентификатор для поиска поста.
        :return: пост.
        """
        posts_data = self.get_posts_all()
        try:
            for post in posts_data:
                if pk == post['pk']:
                    return post
        except ValueError:
            print('Поста по такому "pk" нет')
