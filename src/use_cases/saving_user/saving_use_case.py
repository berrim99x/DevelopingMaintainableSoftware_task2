from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.ports.save_user_output_port import SaveUserOutputPort
from src.entities.user import User
from src.viewmodels.user_view_model import UserViewModel

class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface, presenter: SaveUserOutputPort):
        self.user_repository = user_repository
        self.presenter = presenter

    def execute(self, user: User) -> UserViewModel:
        # Validate user
        if not self._is_valid(user):
            # بناء ViewModel مع رسالة الخطأ
            return UserViewModel(user.first_name, user.last_name, success=False, error_message="Invalid user data")

        # Save user to repository
        self.user_repository.save(user)

        # بناء ViewModel مع النجاح
        return UserViewModel(user.first_name, user.last_name, success=True)

    def _is_valid(self, user: User) -> bool:
        return self._has_valid_length(user.first_name) and self._has_valid_length(user.last_name) and \
            self._has_valid_characters(user.first_name) and self._has_valid_characters(user.last_name)

    def _has_valid_length(self, value: str) -> bool:
        return len(value.strip()) >= 2

    def _has_valid_characters(self, value: str) -> bool:
        return value.isalpha() and bool(value.strip())
