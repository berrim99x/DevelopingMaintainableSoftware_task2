from src.user import User
from src.user_repository_interface import UserRepositoryInterface


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, user: User) -> None:
        if not self._is_valid(user):
            return

        self.user_repository.save(user)

    def _is_valid(self, user: User) -> bool:
        return bool(user.first_name)
