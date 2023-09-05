from typing import Generic, AsyncIterator, TypeVar
from app.core.exceptions import NotFoundException
from ..database.postgre import DatabaseSession
from .AbstractRepository import AbstractRepository
from sqlalchemy.future import Select
from ..domain import EntityModel

# T can only be EntityModel or subtypes
T = TypeVar("T", bound=EntityModel)

class SQLRepository(Generic[T], AbstractRepository[T]):
    def __init__(self, session: DatabaseSession) -> None:
        self._session = session

    async def get(self, params: dict) -> AsyncIterator[T]:
        async with self._session.get() as session:
            session.execute(
                Select.select(T)
            )

    async def id(self, id: int) -> T:
        async with self._session.get() as session:
            async with session.get(T) as record:
                if record is None:
                    raise NotFoundException(T, id)
            return record

    async def add(self, model: T) -> T:
        with self.session_factory() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    async def update(self, id: int) -> bool:
        with self.session_factory() as session:
            try:
                record: T = self.id(id)
                session.delete(record)
                session.commit()
            except Exception as e:
                raise e

    async def delete(self, id: int) -> bool:
        with self.session_factory() as session:
            try:
                record: T = self.get_by_id(id)
                session.delete(record)
                session.commit()
            except Exception as e:
                raise e

