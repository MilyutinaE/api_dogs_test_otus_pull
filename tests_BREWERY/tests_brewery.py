import pytest
import requests


# Проверяем, что List Breweries выдает ответ 200
def test_api_status_code():
    r = requests.get("https://api.openbrewerydb.org/v1/breweries")
    assert r.status_code == 200


# Проверяем, что по нужному айди возвращается верное название пивнухи
@pytest.mark.parametrize("obdb_id, name", [("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "MadTree Brewing 2.0"),
                                           ("ef970757-fe42-416f-931d-722451f1f59c", "10 Barrel Brewing Co")])
def test_obdb_id(obdb_id, name, base_url):
    r_name = requests.get(base_url +  f"/{obdb_id}")
    assert r_name.status_code == 200
    json_name = r_name.json()
    assert json_name["name"] == name


# Делаем поиск по dog в названии пивнухи и проверяем, что в ответе все названия с dog
def test_get_names_with_dog(base_url):
    r_dog = requests.get(base_url + "/autocomplete?query=dog")
    assert r_dog.status_code == 200
    json_dog = r_dog.json()
    for json_dog in json_dog:
        text = json_dog["name"]
        assert "dog" in text.lower()


# Делаем поиск по городу и проверяем, что в ответе только этот город
def test_get_by_sity(base_url):
    r_san_diego = requests.get(base_url + "?by_city=san_diego")
    assert r_san_diego.status_code == 200
    json_san_diego = r_san_diego.json()
    for json_san_diego in json_san_diego:
        text = json_san_diego["city"]
        assert "san diego" in text.lower()


# Проверяем, что в ответе в json 3 пивнухи
def test_size_3(base_url):
    r_size = requests.get(base_url + "/random?size=3")
    assert r_size.status_code == 200
    json_r_size = r_size.json()
    assert len(json_r_size) == 3


# Проверяем поиск по названию пивнухи
@pytest.mark.parametrize("by_name", ('3cross Fermentation Cooperative', '(512) Brewing Co'))
def test_by_name(by_name, base_url):
    query = {'by_name': f'{by_name}'}
    r = requests.get(base_url, params=query)
    assert r.status_code == 200
    json_names = r.json()
    assert json_names[0]['name'] == by_name   #Доступ к элементам списка осуществляется по индексу, без [0] не работает


