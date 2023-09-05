from pydantic import parse_obj_as
from bson.objectid import ObjectId
from sqlalchemy import Column, Integer
from typing import Generic, Iterator, TypeVar

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import DeclarativeMeta
from .DomainModel import DomainModel

D = TypeVar("D", bound=DomainModel)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

class EntityModel(Generic[D], DeclarativeMeta):
    __abstract__ = True
    
    id = Column(Integer(), autoincrement=True, primary_key=True)

    # TODO: Remove ignore
    # https://github.com/sqlalchemy/sqlalchemy/issues/10264
    metadata = MetaData(naming_convention=convention)  # type: ignore

    def __repr__(self) -> str:
        columns = ", ".join(
            [f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith("_")]
        )
        return f"<{self.__class__.__name__}({columns})>"
    
    # Get domain object
    def get(self) -> D:
        return parse_obj_as(D, self)