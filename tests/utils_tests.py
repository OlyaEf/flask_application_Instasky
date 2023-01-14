import pytest

from utils import PostHandler


@pytest.fixture
def post_number_1():
    return [{
    "poster_name": "leo",
    "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
    "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
    "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
    "views_count": 376,
    "likes_count": 154,
    "pk": 1
  }]


@pytest.fixture
def comments_7():
    return [{
    "post_id": 7,
    "commenter_name": "hanna",
    "comment": "Очень необычная фоторафия! Где это?",
    "pk": 20
  }]


def test_get_post_by_pk(post_number_1):
    post_handler = PostHandler()
    post = [post_handler.get_post_by_pk(1)]
    assert post == post_number_1


def test_get_posts_all():
    post_handler = PostHandler()
    len_posts = len(post_handler.get_posts_all())
    assert len_posts == 8


def test_get_posts_by_user():
    post_handler = PostHandler()
    user_post = post_handler.get_posts_by_user('leo')
    assert len(user_post) == 2


def test_get_comments_by_post_id(comments_7):
    post_handler = PostHandler()
    comments = post_handler.get_comments_by_post_id(7)
    assert comments == comments_7


def test_search_for_posts(post_number_1):
    post_handler = PostHandler()
    search_posts = post_handler.search_for_posts('еда')
    assert search_posts == post_number_1
