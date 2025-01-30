
# Тестовое задание 

по мотивам 
<br>
![badge](https://github.com/avito-tech/mi-trainee-task?tab=readme-ov-file)


### Стек технологий

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-%230A9EDC.svg?style=for-the-badge&logo=pytest&logoColor=white)


## Установка 

1. Клонируйте репозиторий на свой компьютер:

    ```bash
    git clone https://github.com/Neitii/test_api_secret
    ```
    ```bash
    cd testovoe
    ```

2. Создайте файл .env и заполните его своими данными (ALLOWED_HOSTS следует заполнять через пробел):
	POSTGRES_DB
	POSTGRES_USER
	POSTGRES_PASSWORD
	DB_NAME
	DB_HOST
	DB_PORT
	SECRET_KEY
	ALLOWED_HOSTS
	DEBUG
	USE_SQLITE 
	

3. Запустите приложение в контейнерах из папки с файлом docker-compose.yml:

```sh
docker-compose up -d --build
```

4. Создайте и выполните миграции, соберите статику:

```sh
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

5. Создайте суперпользователя:

```sh
docker-compose exec backend python manage.py createsuperuser
```

6. Команда для выполнения тестов:
```sh
docker-compose exec backend python -m pytest -v   
```


### Примеры запросов:

Для регистрации нового секрета отправить POST-запрос:

```
POST /generate/
```

```sh
{
  "secret": "надо было тогда не так сказать",
  "passphrase": "мысли перед сном"
}
```


Пример ответа:

```sh
{
  "secret_key": "abrakadabra"
}
```


Для получения секрета отправить POST-запрос на соответвующий secret_key, запрос можно сделать только один:

```
POST secrets/abrakadabra/
```

```sh
{
    "passphrase": "мысли перед сном"
}
```


Пример ответа:
```sh
{
    "secret": "надо было тогда не так сказать"
}
```

### Автор
Тигина Анна
