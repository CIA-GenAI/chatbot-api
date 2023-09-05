from pydantic import BaseModel


class DomainModel(BaseModel):
    _nameapace = ""

    class Config:
        
        from_attributes = True
        arbitrary_types_allowed = True
