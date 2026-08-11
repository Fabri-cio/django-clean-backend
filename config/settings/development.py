from .base import *
from decouple import config


DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]