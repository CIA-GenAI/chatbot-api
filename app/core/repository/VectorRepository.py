from typing import Generic, Iterator

from ..database.weaviate import VectorSession
from .AbstractRepository import AbstractRepository, T

class VectorRepository(Generic[T], AbstractRepository[T]):
    def __init__(self, client: VectorSession) -> None:
        self._client = client

    async def get(self) -> Iterator[T]:
        raise NotImplementedError

    async def id(self, id: int) -> T:
        raise NotImplementedError

    async def add(self, model: T) -> T:
        raise NotImplementedError

    async def update(self, model: T) -> T:
        raise NotImplementedError

    async def delete(self, id: int) -> None:
        raise NotImplementedError

