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
        validators = [
            self._has_first_name,
            self._has_last_name,
        ]
        return all(validator(user) for validator in validators)

    def _has_first_name(self, user: User) -> bool:
        return bool(user.first_name.strip())

    def _has_last_name(self, user: User) -> bool:
        return bool(user.last_name.strip())
