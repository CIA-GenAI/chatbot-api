from pydantic import BaseSettings

from .envs import get_envs

envs = get_envs()


class CelerySettings(BaseSettings):
    broker_url: str = envs.celery_broker_url
    backend_url: str = envs.celery_backend_url