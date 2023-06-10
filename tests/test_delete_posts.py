import requests


def test_delete_posts():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
