# Django ORM Watching Storage

Этот проект — веб-приложение на Django, которое позволяет взаимодействовать с удаленной базой данных PostgreSQL для мониторинга и управления пропусками.

## Требования

Перед запуском проекта убедитесь, что у вас установлены:
- Python 3.2 или более поздняя версия
- Pip (менеджер пакетов Python)

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone <URL вашего репозитория>
   cd django-orm-watching-storage
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Создайте файл `.env`:**
   Скопируйте и отредактируйте пример файла `.env`, чтобы указать нужные переменные окружения.

   Пример:
   ```env
   DATABASE_URL://USER:PASSWORD@HOST:PORT/NAME
   SECRET_KEY=ваш_секретный_ключ
   ALLOWED_HOSTS=localhost,127.0.0.1
   DEBUG=False
   ```


## Запуск

1. **Примените миграции базы данных:**
   ```bash
   python manage.py migrate
   ```

2. **Запустите сервер:**
   ```bash
   python manage.py runserver 
   ```

3. **Откройте в браузере:**
   Перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000), чтобы увидеть работающий сайт.
   Или же можете зайти по адресу: [localhost:8000](http://0.0.0.0:8000)
## Полезные команды Django

- `python manage.py migrate` — применить миграции
- `python manage.py createsuperuser` — создать суперпользователя
- `python manage.py runserver` — запустить локальный сервер

---
