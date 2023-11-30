# API Yatube

## Технологии:
- Python 3.9
- Django 2.2
- Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном

## API социальной сети блогеров **Yatube**
REST API для проекта [YaTube](https://github.com/Ilya-Reznikov/hw05_final)

У неаутентифицированных пользователей есть возможность получить посты пользователей соцсети, комментарии к постам, а также информацию о группах.

Аутентифицированные пользователи могут добавлять посты и комментарии, подписываться на авторов. Также им доступно изменение и удаление своего контента. 

Для аутентификации используются JWT-токены.

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Ilya-Reznikov60/api_yatube
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
## Доступные эндпоинты

- `api/v1/posts/` : получаем список всех постов или создаём новый пост;
- `api/v1/posts/{post_id}/` : получаем, редактируем или удаляем пост по id;
- `api/v1/posts/{post_id}/comments/` : получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать;
- `api/v1/posts/{post_id}/comments/{comment_id}/` : получаем, редактируем или удаляем комментарий по id у поста с id=post_id;
- `api/v1/groups/` : получаем список всех групп;
- `api/v1/groups/{group_id}/` : получаем информацию о группе по id;
- `api/v1/follow/` : получаем все подписки пользователя, сделавшего запрос, или подписываемся на пользователя, переданного в теле запроса;
- `api/v1/jwt/create/` : получение JWT-токена
- `api/v1/jwt/refresh/` : обновление JWT-токена
- `api/v1/jwt/verify/` : проверка JWT-токена


### Автор
Резников Илья - [GitHub](https://github.com/Ilya-Reznikov60)
