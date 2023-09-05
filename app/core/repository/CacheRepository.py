from typing import Generic, Iterator
from app.core.exceptions import NotFoundException
from ..database.redis import CacheSession
from .AbstractRepository import AbstractRepository, T

class CacheRepository(Generic[T], AbstractRepository[T]):
    def __init__(self, session: CacheSession) -> None:
        self.client = session.client

    def get_all(self) -> Iterator[T]:
        raise NotImplementedError

    def get_by_id(self, id: str) -> T:
        data: T = self.client.get(id)
        return data

    def add(self, model: T, specs: dict = None) -> T:
        ttl = specs.ttl if specs else None
        self.client.set(model.id, model, ex = ttl)

    def delete_by_id(self, id: str) -> None:
        self.client.delete(id)
        
    def update(self, model: T) -> None:
        self.client.set(model.id, model)
