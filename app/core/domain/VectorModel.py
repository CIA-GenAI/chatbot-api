from typing import Generic, TypeVar
from .DomainModel import DomainModel

D = TypeVar("D", bound=DomainModel)

class VectorModel(Generic[D]):
    _namespace: str