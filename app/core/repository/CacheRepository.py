from pydantic import parse_obj_as
from typing import Generic, AsyncIterator, TypeVar
from app.core.exceptions import NotFoundException
from ..database.redis import CacheSession
from .AbstractRepository import AbstractRepository
from ..domain import CacheModel

# T can only be CacheModel or subtypes
T = TypeVar("T", bound=CacheModel)

class CacheRepository(Generic[T], AbstractRepository[T]):
    def __init__(self, session: CacheSession) -> None:
        self._session = session

    async def get(self, params: dict) -> AsyncIterator[T]:
        raise NotImplementedError

    async def id(self, id: str) -> T | None:
        async with self._session.get() as client:
            record = await client.get(id)
            return record if record is None else parse_obj_as(T, record)

    async def add(self, model: T, specs: dict = None) -> T:
        ttl = specs.ttl if specs else None
        async with self._session.get() as client:
            await client.set(model.id, model, ex = ttl)

    async def update(self, model: T) -> None:
        async with self._session.get() as client:
            client.set(model.id, model)

    async def delete(self, id: str) -> None:
        async with self._session.get() as client:
            client.delete(id)
                
