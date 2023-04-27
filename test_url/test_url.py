import pytest
import requests


def test_url(url, status_code):
    r_resourse = requests.get(url)
    assert r_resourse.status_code == status_code


#  запускаем в терминале pytest test_url.py --url=https://mail.ru --status_code=200  (можно менять урл и статус код)
# в тесте делается get запрос и проверяется статус код ответа
# если запустить просто pytest test_url.py, возьмутся значения по умолчанию из конфтеста
