import requests


def test_post_posts():
    payload = {
        "title": "Hi there",
        "body": "The first one",
        "userId": 1
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data=payload)
    assert response.status_code == 201

    data = response.json()
    assert data['title'] == "Hi there"
    assert data['body'] == "The first one"
    assert int(data['userId']) == 1  # преобразуем 'userId' в число перед сравнением
