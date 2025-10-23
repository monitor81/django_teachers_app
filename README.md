# Django Teachers Management App

Приложение для управления преподавателями и дисциплинами с использованием Django, Docker и PostgreSQL.

## Функциональность

- Добавление преподавателей
- Управление дисциплинами
- Поиск по преподавателям и дисциплинам
- Docker контейнеризация
- PostgreSQL база данных

## Технологии

- Django 4.2
- PostgreSQL
- Docker & Docker Compose
- Tailwind CSS

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/monitor81/django_teachers_app.git
cd django_teachers_app 
```

2. Создайте файл .env:

POSTGRES_DB=teachers_db
POSTGRES_USER=teachers_user
POSTGRES_PASSWORD=teachers_password
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

3. Запустите приложение:
```bash
docker-compose up --build
```
4. Выполните миграции (в новом терминале):

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
5. Откройте в браузере: http://localhost:8000