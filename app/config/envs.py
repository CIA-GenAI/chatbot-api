from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Envs(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow')

@lru_cache()
def get_envs():
    return Envs()