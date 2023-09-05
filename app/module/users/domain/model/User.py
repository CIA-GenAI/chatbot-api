from datetime import datetime

from pydantic import Field

from app.core.domain.DomainModel import DomainModel


class User(DomainModel):
    email: str = Field(None, description="Email")
    nickname: str = Field(None, description="Nickname")
    is_admin: bool = Field(False, description="Is admin")
    created_at: datetime = Field(None, description="Create Time")
    updated_at: datetime = Field(None, description="Update Time")
