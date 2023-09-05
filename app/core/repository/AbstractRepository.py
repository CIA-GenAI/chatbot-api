from abc import ABC, abstractmethod
from typing import Generic, AsyncIterator, TypeVar

from ..domain import EntityModel, DocumentModel, CacheModel, VectorModel


# T can only be EntityModel or DocumentModel or subtypes of either
T = TypeVar("T", bound=EntityModel|DocumentModel|CacheModel|VectorModel)

class AbstractRepository(Generic[T], ABC):

  @abstractmethod
  async def get(params: dict) -> AsyncIterator[T] | None:
    raise NotImplementedError

  @abstractmethod
  async def id(id: int|str) -> T | None:
    raise NotImplementedError

  @abstractmethod
  async def add(model: T, specs: dict = None) -> T | None:
    raise NotImplementedError

  @abstractmethod
  async def update(model: T) -> T | None:
    raise NotImplementedError

  @abstractmethod
  async def delete(id: int|str) -> bool:
    raise NotImplementedError