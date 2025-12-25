from src.entities.user import User
from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, user: User) -> None:
        if not self._is_valid(user):
            return

        self.user_repository.save(user)

    def _is_valid(self, user: User) -> bool:
        return self._has_valid_length(user.first_name) and \
               self._has_valid_length(user.last_name) and \
               self._has_valid_characters(user.first_name) and \
               self._has_valid_characters(user.last_name)

    def _has_valid_length(self, value: str) -> bool:
        return len(value.strip()) >= 2

    def _has_valid_characters(self, value: str) -> bool:
        return value.isalpha() and bool(value.strip())

