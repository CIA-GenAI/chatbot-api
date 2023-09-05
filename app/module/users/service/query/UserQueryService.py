from typing import Iterable, Optional
from app.module.users.exception import UserNotFoundException
from app.module.users.repository.UserRepository import UserRepository
from app.module.users.domain.model.User import User

class UserQueryService:

    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo

    async def get_by_id(self, id: int) -> Optional[User]:
        user = await self._user_repo.get_all(id)
        if not user:
            raise UserNotFoundException
        return User(user)
    
    async def get_all(self) -> Optional[Iterable[User]]:
        users = await self._user_repo.get_all()
        return users

