## Запускаем микросервис в Docker  
1. Создать `Dockerfile`  
[FastApi in containers](https://fastapi.tiangolo.com/deployment/docker/#what-is-a-container-image)   
2. Выбрать версию Docker образа:  
[hub.docker.com](https://hub.docker.com/_/python)    
3. Настроить Dockerfile указав необходимые команды и зависимости  
4. Выполнить сборку образа. Команда:  
```commandline
docker build . -t qa-guru-app
```
5. Проверка образа командой  
```commandline
docker images
```
6. Запуск Docker образа командой 
```commandline
docker run qa-guru-app
```
mapping ports  - command `-p 8002:80`

```commandline
docker run -e DATABASE_ENGINE=postgresql+psycopg2://postgres:123456@localhost:5432/postgres -p 8002:80 qa-guru-app

```
Запускаем `docker compose up`

Вместо localhost пропишем хост компьютера (локального) и финальная команда
```commandline
docker run -e DATABASE_ENGINE=postgresql+psycopg2://postgres:123456@host.docker.internal:5432/postgres -p 8002:80 qa-guru-app

```

После переноса переменной DATABASE_ENGINE в Dockerfile запуск проекта осуществляется командой
```commandline
docker compose up
```

Убираем пароль и имя пользователя в env файл через использование переменных ${DATABASE_USER}  
Тк имя переменной POSTGRES_PASSWORD у нас совпадете с db  - то там просто оставляем как есть  

```yaml
    environment:
    # Use github secrets
      POSTGRES_PASSWORD:
```

# Используем официальный образ Python