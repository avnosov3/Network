## Описание проекта
Проект представляет собой простое RESTful API, разработанное с использованием FastAPI, для социальной сети. В API реализована возможность аутентификации и регистрации пользователей с использованием JWT. Пользователь  может создавать новые посты, редактировать их содержимое, удалять собственные посты и просматривать существующие посты и ставить им лайки.

## Техно-стек
* python 3.10
* fastapi 0.78.0
* aiosqlite 0.17.0
* sqlalchemy 1.4.36
* alembic 1.7.7
* uvicorn 0.17.6
* fastapi-users 10.0.6

## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке

```
git clone git@github.com:avnosov3/webtronics-test-task.git
cd webtronics-test-task/
```

Создать .env и заполнить

```
DATABASE_URL=sqlite+aiosqlite:///./megatronics_net.db
SECRET=<Укажите секрет>
```

Запустить docker compose

```
docker compose up -d
```

Провести миграции

```
docker compose exec webtronics poetry run alembic upgrade head
```

# Документация
После запуска документация будет доступна в виде
* [swagger](http://127.0.0.1:8000/docs/)
* [redoc](http://127.0.0.1:8000/redoc/)
