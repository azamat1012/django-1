from environs import Env
import os

# Инициализация environs
env = Env()
env.read_env()

# Получаем переменные окружения
ENGINE = env.str("ENGINE")
HOST = env.str("HOST")
PORT = env.int("PORT")
NAME = env.str("NAME")
USER = env.str("user")
PASSWORD = env.str("PASSWORD")

DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool("DEBUG", default=False)


ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
