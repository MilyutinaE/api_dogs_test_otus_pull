import pytest
import requests


# Проверяем, что сам сайт работает
def test_api_status_code():
    r = requests.get("https://dog.ceo/dog-api/")
    assert r.status_code == 200


# Проверяем, что у породы australian есть подвид, а у породы afghan нет подвида
@pytest.mark.parametrize("hound, output", [("australian", "success"), ("afghan", "error")])
def test_get_hound_list(hound, output, base_url):
    r_hound = requests.get(base_url + f"/breed/{hound}/list")
    json_hound = r_hound.json()
    assert json_hound["status"] == output


# Сохраняем рандомную картинку породы
def test_get_random_jpg(base_url):
    r_jgp = requests.get(base_url + "/breeds/image/random")
    assert r_jgp.status_code == 200
    json_jgp = r_jgp.json()
    jimg_file = json_jgp["message"]
    r_jgp = requests.get(jimg_file)
    out = open("breed_image_random.jpg", "wb")
    out.write(r_jgp.content)
    out.close()


# Проверяем, что в ответе в json подвидов > 0 (вообще всех подвидов)
def test_list_sub_breeds(base_url):
    r_sub_breed = requests.get(base_url + "/breed/hound/list")
    assert r_sub_breed.status_code == 200
    json_sub_breed = r_sub_breed.json()
    assert len(json_sub_breed['message'])
    # assert len(respone) > 0 - не надо писать больше 0. ассерт сработает пасс и так, если будет больше 0


# Проверяем, что в ответе будет не больше 50ти картинок (Max number returned is 50)
@pytest.mark.parametrize("count_images", (49,50,51))
def test_max_number_images(count_images, base_url):
    r_max_images = requests.get(base_url + f"/breeds/image/random/{count_images}")
    assert r_max_images.status_code == 200
    json_max_images = r_max_images.json()
    assert len(json_max_images['message']) <= 50



