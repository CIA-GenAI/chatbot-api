from typing import Generic, Iterator

from ..database.weaviate import VectorClient
from .AbstractRepository import AbstractRepository, T

class VectorRepository(Generic[T], AbstractRepository[T]):
    def __init__(self, client: VectorClient) -> None:
        self._client = client

    def get_all(self) -> Iterator[T]:
        raise NotImplementedError

    def get_by_id(self, id: int) -> T:
        raise NotImplementedError

    def add(self, model: T) -> T:
        raise NotImplementedError

    def delete_by_id(self, id: int) -> None:
        raise NotImplementedError

