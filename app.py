from flask import Flask, render_template, request
from utils import PostHandler

post_handler = PostHandler()

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
