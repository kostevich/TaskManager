# TaskManager
**TaskManager** – учебный проект на [Django](https://www.djangoproject.com/), позволяющий создавать и отслеживать задачи.
Имеются такие параметры как: состояние задачи, повторение задачи.

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать. 
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [Django](https://github.com/django/django?ysclid=lph3fmn0za256973455) не старше 4.2.1.
```
pip install Django
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. В среде исполнения запустить файл _manage.py_ командой:
```
python manage.py runserver
```
5. Перейти по ссылке (пример: http://127.0.0.1:8000/).

# Отслеживание данных в адмиистративной панели Django.
1. В среде исполнения запустить команду:
```
python manage.py createsuperuser
```
2. Зарегистрироваться.
3. Перейти по ссылке добавив к ней admin (пример: http://127.0.0.1:8000/admin).

# Отслеживание в базе данных.

Откройте файл db.sqlite3 в программе для открытия баз данных (пример: [SQLiteStudio](https://sqlitestudio.pl/)).

# Пример работы

**Список задач:**

![image](https://github.com/kostevich/TaskManager/assets/109979502/ed7f70d5-d4f7-4708-9cd1-1234ec108a86)

**Создание новой задачи:**

![image](https://github.com/kostevich/TaskManager/assets/109979502/280d9ad7-8ba4-4cd8-970e-eab8b9eeff41)

_Copyright © Kostevich Irina. 2023._
