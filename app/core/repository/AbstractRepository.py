from abc import ABC, abstractmethod
from typing import Generic, Iterator, TypeVar

from ..domain.DomainModel import DomainModel

# T can only be DomainModel or subtype of DomainModel
T = TypeVar("T", bound=DomainModel)

class AbstractRepository(Generic[T], ABC):

  @abstractmethod
  def get_all() -> Iterator[T] | None:
    raise NotImplementedError

  @abstractmethod
  def get_by_id(id) -> T | None:
    raise NotImplementedError

  @abstractmethod
  def add(model: T, specs: dict = None) -> T | None:
    raise NotImplementedError

  @abstractmethod
  def update(model: T) -> T | None:
    raise NotImplementedError

  @abstractmethod
  def delete(id) -> bool:
    raise NotImplementedError