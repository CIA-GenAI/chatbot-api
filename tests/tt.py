from pydantic import BaseModel
from typing import Generic, TypeVar, Type

class DomainModel(BaseModel):
    _nameapace = ""


D = TypeVar("D", bound=DomainModel)

class CacheModel(Generic[D]):
    _namespace: str
    

class User:
    _namespace: str

