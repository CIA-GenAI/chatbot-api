from dotenv import dotenv_values
from functools import lru_cache

class Envs(dict):
    __getattr__ = dict.__getitem__

@lru_cache()
def get_envs():
    return Envs({k.lower():v for k,v in dotenv_values(".env").items()})