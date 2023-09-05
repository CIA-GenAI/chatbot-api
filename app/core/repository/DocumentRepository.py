from typing import Generic, Iterator, TypeVar, cast
from app.core.exceptions import NotFoundException
from pymongo.collection import Collection
from ..database.mongo import DocumentSession
from .AbstractRepository import AbstractRepository, T
from ..domain import DocumentModel
from .exception import DocumentDomainRequiredError
from ..domain import CacheModel

# T can only be CacheModel or subtypes
T = TypeVar("T", bound=CacheModel)

class DocumentRepository(Generic[T], AbstractRepository[T]):

    def __init__(self,
                 session: DocumentSession,
                 collection_name: str) -> None:

        self.collection: Collection = None

        if isinstance(T, DocumentModel):
            self.collection = session.get_db().get_collection(collection_name)
        else:
            raise DocumentDomainRequiredError


    async def get(self) -> Iterator[T]:
        with self.session_factory() as session:
            return session.query(T).all()

    async def id(self, id: int) -> T:
        with self.session_factory() as session:
            record: T = session.query(T).filter(T.id == id).first()
            if not record:
                raise NotFoundException(T, id)
            return record

    async def add(self, model: T) -> T | None:
        with self.session_factory() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    async def update(self, model: T) -> bool:
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
                record: T = self.id(id)
                session.delete(record)
                session.commit()
            except Exception as e:
                raise e

