## Запускаем микросервис в Docker

Preconditions - run `Docker descktop.exe`

### Последовательная сборка шаг за шагом, с постепенным улучшением кода и расширением `dockerfile`

1. Создать `Dockerfile`  
   [FastApi in containers](https://fastapi.tiangolo.com/deployment/docker/#what-is-a-container-image)
2. Выбрать версию Docker образа:  
   Использовать лучше официальные версии образов  
   [hub.docker.com](https://hub.docker.com/_/python)
3. Настроить Dockerfile указав необходимые команды и зависимости
4. Выполнить сборку образа. Команда:

```commandline
docker build . -t qa-guru-app
```

В дальнейшем - при любом изменении в проекте необходимо заново пересобирать образ

5. Проверка образа командой

```commandline
docker images
```

6. Запуск Docker образа командой

```commandline
docker run qa-guru-app
```

Настройка внешних портов mapping ports в строке команды используем - command

```commandline
-p 8002:80
```

7. Запуск контейнера с подключением к базе данных

```commandline
docker run -e DATABASE_ENGINE=postgresql+psycopg2://postgres:123456@localhost:5432/postgres -p 8002:80 qa-guru-app

```

Запускаем `docker compose up`

8. Вместо localhost пропишем хост компьютера (локального) и финальная команда

```commandline
docker run -e DATABASE_ENGINE=postgresql+psycopg2://postgres:123456@host.docker.internal:5432/postgres -p 8002:80 qa-guru-app

```

9. Перенос переменной DATABASE_ENGINE  
   После переноса переменной `DATABASE_ENGINE` в Dockerfile запуск проекта осуществляется командой

```commandline
docker compose up
```

10. Убираем пароль и имя пользователя в env файл через использование переменных ${DATABASE_USER}  ${POSTGRES_PASSWORD}  
    Тк имя переменной POSTGRES_PASSWORD у нас совпадете с db - то там просто оставляем как есть

```yaml
    environment:
      # Use github secrets
      POSTGRES_PASSWORD:
```

11. Добавим файл `.dockerignore`

### Финальная последовательность запуска проекта в Docker:

- Запуск Docker локально десктоп версия
- запуск приложения в контейнере командой `docker compose up`
- запуск тестов командой `pytest`
- остановка и закрытие сервера/контейнера командой `docker compose down`

## Деплоим микросервис с Github Actions.

1. Настроим деплой микросервиса с Github Actions.
2. Обновим тесты  
   [События для запуска workflow](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#pull_request)  
   [Git и GitHub flow](https://medium.com/@yanminthwin/understanding-github-flow-and-git-flow-957bc6e12220)  
3. Update dockerfile - fix minor mistakes  


### Start project:  
1. Create directory `.github` -> `workflows`
2. create `test.yml`
   - Add parameters [github actions](), 
   - Add [setup-python](https://github.com/actions/setup-python)  
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.13' 
- run: python my_script.py
```
3. Commit and push code to Github
4. Create pull_requests -> Actions  
5. Good action to add useful logs to our actions: [pytest result actions](https://github.com/pmeier/pytest-results-action)
add to `test.yml`:  
```yaml
   - run: pytest tests --junit-xml=test-results.xml
```
6. Add password to repository secret and variables options. `settings->secret and variables->actions`  
7. 


