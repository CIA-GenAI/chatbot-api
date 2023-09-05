from pydantic import BaseSettings

from .envs import get_envs

envs = get_envs()


class OpenAPISettings(BaseSettings):
    title: str = envs.openapi_title
    description: str = envs.openapi_description
    version: str = envs.openapi_version