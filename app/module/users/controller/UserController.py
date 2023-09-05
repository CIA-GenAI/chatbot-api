from typing import Optional, List
from app.module.users.domain.model.User import User
from app.core.controller import BaseController
from sqlalchemy.orm import Session
from ..service.command.UserCommandService import UserCommandService
from ..service.query.UserQueryService import UserQueryService


class UserController(BaseController):

    def __init__(self,
                 user_cs: UserCommandService,
                 user_qs: UserQueryService) -> None:

        self._user_cs: UserCommandService = user_cs
        self._user_qs: UserQueryService = user_qs

    def get_all(self):
        return self._user_qs.get_all()

    def get_by_id(self, id: int):
        return self._user_qs.get_by_id(id)