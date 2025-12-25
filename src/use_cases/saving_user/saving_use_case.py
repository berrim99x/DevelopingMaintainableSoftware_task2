from src.entities.user import User
from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.ports.save_user_output_port import SaveUserOutputPort


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface, presenter: SaveUserOutputPort):
        self.user_repository = user_repository
        self.presenter = presenter

    def execute(self, user: User) -> None:

        if not self._is_valid(user):
            self.presenter.present_error("Invalid user data")
            return

        self.user_repository.save(user)
        self.presenter.present_success()

    def _is_valid(self, user: User) -> bool:
        return self._has_valid_length(user.first_name) and self._has_valid_length(user.last_name) and \
               self._has_valid_characters(user.first_name) and self._has_valid_characters(user.last_name)

    def _has_valid_length(self, value: str) -> bool:
        return len(value.strip()) >= 2

    def _has_valid_characters(self, value: str) -> bool:
        return value.isalpha() and bool(value.strip())
