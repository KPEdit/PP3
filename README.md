Скачать и установить (при установке введите пароль 999bk):
https://www.postgresql.org/download/

1) Найти через меню-пуск "SQL Shell (psql)"
2) использовать настройки по умолчанию (4 раза нажать Enter), после ввести пароль 999bk.
3) postgres=# CREATE DATABASE bkdb; - создат дб bkdb, к которой подключится сайт
=========
1) Склонировать репозиторий
2) В папке с manage.py запустить cmd
3) В консоли: python manage.py makemigrateions bk_parser
4) В консоли: python manage.py migrate
5) В консоли: python manage.py createsuperuser - откроется панелька, в которой придется создать суперпользователя (Superuser created successfully - аккаунт админа создан)
6) В консоли: python manage.py runserver - запустит локальный сервер на вашей машине
7) Перейти в браузере по адресу 127.0.0.1:8000/admin/ - и залогиньтся с помощью аккаунта админа
8) Вауля!

Файлы для front-ender'a находятся в bk_parser/templates (html файлы) и bk_parser/static (css и js файлы)
