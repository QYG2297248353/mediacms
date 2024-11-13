import os

# Fetch environment variables with default values
FRONTEND_HOST = os.getenv('FRONTEND_HOST', 'http://localhost')
PORTAL_NAME = os.getenv('PORTAL_NAME', 'MediaCMS')
SECRET_KEY = os.getenv('SECRET_KEY', 'ma!s3^b-cw!f#7s6s0m3*jx77a@riw(7701**(r=ww%w!2+yk2')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'db')
REDIS_LOCATION = os.getenv('REDIS_LOCATION', 'redis://redis:6379/1')

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME', 'mediacms'),
        "HOST": POSTGRES_HOST,
        "PORT": os.getenv('DB_PORT', '5432'),
        "USER": os.getenv('DB_USER', 'mediacms'),
        "PASSWORD": os.getenv('DB_PASSWORD', 'mediacms'),
    }
}

# Caching settings
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY STUFF
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = BROKER_URL

MP4HLS_COMMAND = os.getenv('MP4HLS_COMMAND', '/home/mediacms.io/bento4/bin/mp4hls')

DEBUG = os.getenv('DEBUG', 'False') == 'True'
