from flask import Blueprint, jsonify
from utils import PostHandler

import logging, datetime


post_handler = PostHandler()
api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts', methods=['GET'])
def get_all_posts():
    """
    Представление, которое обрабатывает запрос GET /api/posts.
    :return: возвращает полный список постов в виде JSON-списка.
    """
    logging.info('Запросы /api_bp/posts')
    result = post_handler.get_posts_all()
    return jsonify(result)


@api_blueprint.route('/api/posts/<post_id>', methods=['GET'])
def get_post_by_id(post_id):
    """
    Представление, которое обрабатывает запрос GET /api/posts/<post_id>.
    :param post_id: идентификационный номер поста.
    :return: возвращает один пост в виде JSON-словаря.
    """
    logging.info(f'{datetime.datetime.now()} [INFO] Запрос api_bp/posts/{post_id}')
    return jsonify(post_handler.get_post_by_pk(post_id))


