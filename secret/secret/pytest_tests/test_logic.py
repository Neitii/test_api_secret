import pytest
from http import HTTPStatus
from django.urls import reverse
from secret_project.models import Secret

pytestmark = pytest.mark.django_db


def test_created_secret(client, form_data):
    url = reverse('generate')
    response = client.post(url, data=form_data)

    assert response.status_code == HTTPStatus.CREATED

    secret_count = Secret.objects.count()
    assert secret_count == 1

    secret = Secret.objects.get()
    assert secret.secret == form_data['secret']
    assert secret.passphrase == form_data['passphrase']


def test_not_get_url(client, form_data, phrase_data):
    url = reverse('generate')
    response = client.post(url, data=form_data)

    url = reverse('secret', kwargs={'key': 'not_secret_key'})
    response = client.post(url, data=phrase_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    secret_count = Secret.objects.count()
    assert secret_count == 1


def test_not_get_passphrase(client, form_data, not_phrase_data):
    url = reverse('generate')
    response = client.post(url, data=form_data)
    secret = Secret.objects.get()

    url = reverse('secret', kwargs={'key': secret.secret_key})

    response = client.post(url, data=not_phrase_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    secret_count = Secret.objects.count()
    assert secret_count == 1


def test_can_get_secret(client, form_data, phrase_data):
    url = reverse('generate')
    response = client.post(url, data=form_data)
    secret = Secret.objects.get()

    url = reverse('secret', kwargs={'key': secret.secret_key})
    response = client.post(url, data=phrase_data)

    status = response.status_code
    assert status == HTTPStatus.OK

    secret_count = Secret.objects.count()
    assert secret_count == 0



# В одном тесте
# @pytest.fixture
# def created_secret(client, form_data):
#     url = reverse('generate')
#     response = client.post(url, data=form_data)
#     assert response.status_code == HTTPStatus.CREATED
#     return Secret.objects.get()


# def test_get_secret(client, created_secret, form_data, not_phrase_data):
#     # Проверяем наличие записи в базе
#     secret_count = Secret.objects.count()
#     assert secret_count == 1
#     secret = Secret.objects.get()
#     assert secret.secret == form_data['secret']
#     assert secret.passphrase == form_data['passphrase']

#     # Используем ключ созданного секрета
#     test_secret_key = created_secret.secret_key

#     # Проверяем попытку доступа к несуществующему секрету
#     url = reverse('secret', kwargs={'key': 'not_secret_key'})
#     response = client.post(url, data=form_data)
#     assert response.status_code == HTTPStatus.BAD_REQUEST

#     # Проверяем доступ к существующему секрету с неправильным паролем
#     url = reverse('secret', kwargs={'key': test_secret_key})
#     response = client.post(url, data=not_phrase_data)
#     assert response.status_code == HTTPStatus.BAD_REQUEST

#     # Проверяем попытку доступа к секрету и его последующее удаление
#     url = reverse('secret', kwargs={'key': test_secret_key})
#     response = client.post(url, data=form_data)
#     status = response.status_code
#     assert status == HTTPStatus.OK
#     secret_count = Secret.objects.count()
#     assert secret_count == 0