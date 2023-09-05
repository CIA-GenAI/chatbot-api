from typing import Optional, List
from app.module.users.domain.model.User import User
from app.core.controller import BaseController
from sqlalchemy.orm import Session
from app.module.users.service.command.UserCommandService import UserCommandService
from app.module.users.service.query.UserQueryService import UserQueryService


class CredentialsController(BaseController):

    def __init__(self,
                 credential_cs: UserCommandService,
                 user_cs: UserCommandService,
                 user_qs: UserQueryService) -> None:

        self._user_cs: UserCommandService = user_cs
        self._user_qs: UserQueryService = user_qs

    def get_or_create(self):
        return self._user_qs.get_all()

    def get_by_id(self, id: int):
        return self._user_qs.get_by_id(id)