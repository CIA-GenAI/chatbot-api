from .api import APISettings
from .openapi import OpenAPISettings
from .database import DatabaseStettings
from .celery import CelerySettings

class Settings():
    api = APISettings()
    openapi = OpenAPISettings()
    database = DatabaseStettings()
    celery = CelerySettings()
