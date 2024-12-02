# Бэкенд сервис для работы со спортивными достижениями участников соревнований

## О проекте
Данный сервис написан с помощью таких технологий:
* Python 3.12
* FastAPI
* SQLAlchemy

Сервис в качестве БД пока использует только **PostgreSQL**. В дальнейшем можно подправить логику работы сервиса
для возможности использовать различные БД.

Для деплоя используется **Docker** и его механизм **docker compose**

## Как запустить
Для запуска сервиса вам необходим установленный docker на вашем ПК

1) Перейдите в корневую папку проекта
2) В терминале хоста выполните команду ``docker compose up --build``
3) Дождитесь загрузки и полного развертывания контейнеров
4) В другом терминале хоста исполните команду ``docker exec -it <id_контейнера_с_fastapi> bash``
5) В терминале контейнера исполните команду ``python src/main.py --prepare-db``

Сервис готов к работе!

> Крайне желательно очищать БД после каждого завершения работы с сервисом посредсвтом введения
> команды ``python src/main.py --clean-db`` в терминале контейнера fast-api

## Как начать работать
По пути ``http://127.0.0.1:80/docs`` работает **Swagger** - интерактивная документация API сервиса.
Вы можете ее изучить и позапускать прямо там различные доступные эндпоинты API