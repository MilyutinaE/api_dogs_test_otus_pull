import pytest
import requests


# Проверяем Resources (100 posts и 10 users)  (Listing all resources)
@pytest.mark.parametrize("resourse, output", [("posts", 100), ("users", 10)])
def test_count_resourses(resourse, output, base_url):
    r_resourse = requests.get(base_url + f"/{resourse}")
    r_json = r_resourse.json()
    assert r_resourse.status_code == 200
    assert len(r_json) == output


# Создаем пост (Creating a resource)
def test_create_post(base_url, input_id='12223', input_title='abobus title bebebe', body='abobus body bababa'):
    r_resourse = requests.post(url=base_url + "/posts", data={'title': input_title, 'body': body, 'userId': input_id})
    r_json = r_resourse.json()
    assert r_resourse.status_code == 201
    assert r_json['title'] == input_title
    assert r_json['body'] == body
    assert r_json['userId'] == input_id


# Удаляем пост, проверяем, что ответ пустой (Deleting a resource)
def test_delete_post(base_url):
    r_resourse = requests.delete(base_url + "/posts/1")
    assert r_resourse.status_code == 200
    r_json = r_resourse.json()
    assert r_json == {}


# Проверяем, что у постов есть комментарии, а у альбомов есть фотографии (Listing nested resources)
@pytest.mark.parametrize("resourse, resourse2", [("posts", "comments"), ("albums", "photos")])
def test_nested_resourses(resourse, resourse2, base_url):
    r_resourse = requests.get(base_url + f"/{resourse}" + f"/1/{resourse2}")
    r_json = r_resourse.json()
    assert r_resourse.status_code == 200
    assert len(r_json)
    print(str(len(r_json)) + " " + resourse2)


# Проверяем, что по ссылке у 1 юзера только посты с userId = 1(Filtering resources)
def test_user_1_posts(base_url):
    r_resourse = requests.get(base_url + "/posts?userId=1")
    r_json = r_resourse.json()
    assert r_resourse.status_code == 200
    for post in r_json:
        assert post["userId"] == 1

