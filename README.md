# webtronics-test-task

# запуск проекта
Проект можно запустить через docker или скачать репозиторий с github

# Docker

```
docker run --name webtronics -it -p 8000:80 avnosov/webtronics:v1
```

# GitHub


Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:avnosov3/webtronics-test-task.git
```

Создать виртуальное окружение

```
cd webtronics-test-task/
poetry env use python
```

Установить зависимости

```
poetry install --no-root
```

Создать .env и заполнить

```
DATABASE_URL=sqlite+aiosqlite:///./megatronics_net.db
SECRET=<Укажите секрет>
```

Провести миграции
```
poetry run alembic upgrade head
```

Запустить проект

```
poetry run uvicorn app.main:app
```

# Документация

После запуска документация будет доступна в виде
* [swagger](http://127.0.0.1:8000/docs/)
* [redoc](http://127.0.0.1:8000/redoc/)


