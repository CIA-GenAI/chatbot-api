from pydantic_settings import BaseSettings

from .envs import get_envs

envs = get_envs()

class APISettings(BaseSettings):
    name: str = envs.app_name
    description: str = envs.app_description
    environment: str = envs.app_environment
    version: str = envs.app_version
    debug: str = envs.app_debug
    key: str = envs.app_apikey
    host: str = envs.app_host
    port: str = envs.app_port
    namespace: str = envs.app_namespace
