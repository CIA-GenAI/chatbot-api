from typing import Generic, Iterator
from app.core.exceptions import NotFoundException
from ..database.postgre import DatabaseSession
from .AbstractRepository import AbstractRepository, T

class InMemoryRepository(Generic[T], AbstractRepository[T]):
    def __init__(self, session: DatabaseSession) -> None:
        self.session_factory = session._factory()

    async def get(self, params: dict) -> Iterator[T]:
        with self.session_factory() as session:
            return session.query(T).all()

    async def id(self, id: int) -> T:
        with self.session_factory() as session:
            record: T = session.query(T).filter(T.id == id).first()
            if not record:
                raise NotFoundException(T, id)
            return record

    async def add(self, model: T) -> T:
        with self.session_factory() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    async def delete(self, id: int) -> bool:
        with self.session_factory() as session:
            try:
                record: T = self.id(id)
                session.delete(record)
                session.commit()
            except Exception as e:
                raise e

