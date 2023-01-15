from flask import Flask, render_template, request, Blueprint, jsonify
from utils import PostHandler

import logging, datetime

app = Flask(__name__)
post_handler = PostHandler()
api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(filename='./logs/basic.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


@app.route('/')
def main_page():
    """
    Представление выводит все посты на главной странице.
    :return: все посты.
    """
    data_posts = post_handler.get_posts_all()
    return render_template('index.html', data_posts=data_posts)


@app.route('/posts/<int:post_id>/')
def page_post(post_id):
    """
    Представление выводит один пост и комментарии к этому посту по идентификационному номеру.
    :param post_id: заданный идентификационный номер поста.
    :return: пост и его комментарии.
    """
    post = post_handler.get_post_by_pk(post_id)
    comments = post_handler.get_comments_by_post_id(post_id)
    count_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@app.route('/search/')
def search():
    """
    Представление для поиска по маршруту.
    :return: все посты в которых присутствует данное слово.
    """
    key_word = request.args.get('s')
    post_search = post_handler.search_for_posts(key_word)
    len_posts = len(post_search)
    return render_template('search.html', post_search=post_search, key_word=key_word, len_posts=len_posts)


@app.route('/users/<username>/')
def posts_user(username):
    """
    Представление с выводом постов конкретного пользователя.
    :param username: 
    :return: посты конкретного по
    """
    user_posts = post_handler.get_posts_by_user(username)
    return render_template('user-feed.html', user_posts=user_posts)


@app.errorhandler(404)
def page_not_found(e):
    """
    Обработчик запросов к несуществующим страницам.
    :param e: выводит 'Ошибка 404, Страница отсутствует'.
    :return: возвращает статус-код 404.
    """
    # устанавливаем статус 404 явно
    return render_template('Ошибка 404, Страница отсутствует'), 404


@app.errorhandler(500)
def page_not_found(e):
    """
    Обработчик ошибок, возникших на стороне сервера.
    :param e: выводит 'Ошибка 500, Внутренняя ошибка сервера'.
    :return: возвращает статус код 500.
    """
    # устанавливаем статус 500 явно
    return render_template('Ошибка 500, Внутренняя ошибка сервера'), 500


@api_blueprint.route('/api/posts', methods=['GET'])
def get_all_posts():
    logging.info('Запросы /api/posts')
    result = post_handler.get_posts_all()
    return jsonify(result)


@api_blueprint.route('/api/posts/<post_id>', methods=['GET'])
def get_post_by_id(post_id):
    logging.info(f'{datetime.datetime.now()} [INFO] Запрос /api/posts/{post_id}')
    return jsonify(post_handler.get_post_by_pk(post_id))


if __name__ == '__main__':
    app.run(debug=True)
