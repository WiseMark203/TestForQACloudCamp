import requests

def test_get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)


def test_get_posts_with_userid():
    response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert all(item['userId'] == 1 for item in data)
