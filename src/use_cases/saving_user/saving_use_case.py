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
        validators = [
            lambda u: self._has_text(u.first_name),
            lambda u: self._has_text(u.last_name),
        ]
        return all(validator(user) for validator in validators)

    def _has_text(self, value: str) -> bool:
        return bool(value and value.strip())
