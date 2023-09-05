from app.module.users.repository.UserRepository import UserRepository
from app.module.users.repository.UserRepository import UserRepository
from app.module.users.domain.model.User import User

class UserCommandService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def create_user(self, user: User) -> User:
        return self._repository.add(user)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
