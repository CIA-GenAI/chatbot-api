from pydantic_settings import BaseSettings

from .envs import get_envs

envs = get_envs()


class CelerySettings(BaseSettings):
    brokerURL: str = envs.celery_broker_url
    backendURL: str = envs.celery_backend_url