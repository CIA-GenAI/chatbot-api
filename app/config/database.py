from pydantic_settings import BaseSettings

from .envs import get_envs

envs = get_envs()

class WeAviateSettings(BaseSettings):  
    url: str = envs.weaviate_url
    api_key: str = envs.weaviate_apikey
    cohere_api_key: str = envs.weaviate_cohere_apikey

class RedisSettings(BaseSettings):
    user: str = envs.redis_user
    host: str = envs.redis_host
    port: str = envs.redis_port
    pwd: str = envs.redis_pwd

class PostgreDBSettings(BaseSettings):
    db: str = envs.pg_db
    port: int = envs.pg_port
    host: str = envs.pg_host
    user: str = envs.pg_user
    pwd: str = envs.pg_pwd

class MongoDBSettings(BaseSettings):
    host: str = envs.documents_host
    port: str = envs.documents_port
    db: str = envs.documents_db
    user: bool = envs.documents_user
    pwd: int = envs.documents_pwd
    debug: bool = envs.documents_debug
    
class SQLiteSettings:
    url: str = envs.sqlite_url

# Aggregate all database settings

class DatabaseStettings:
    weaviate: WeAviateSettings
    redis: RedisSettings
    postgre: PostgreDBSettings
    mongo: MongoDBSettings
    sqlite:SQLiteSettings

        
    