from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.ports.save_user_output_port import SaveUserOutputPort
from src.entities.user_dto import UserDTO
from src.viewmodels.user_view_model import UserViewModel

class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface, presenter: SaveUserOutputPort):
        self.user_repository = user_repository
        self.presenter = presenter

    def execute(self, user_dto: UserDTO) -> UserViewModel:
        if not self._is_valid(user_dto):
            # بناء ViewModel مع رسالة الخطأ
            return UserViewModel(user_dto.first_name, user_dto.last_name, success=False, error_message="Invalid user data")

        # Save user to repository
        self.user_repository.save(user_dto)

        # Notify success
        self.presenter.present_success()

        # بناء ViewModel مع النجاح
        return UserViewModel(user_dto.first_name, user_dto.last_name, success=True)

    def _is_valid(self, user_dto: UserDTO) -> bool:
        return self._has_valid_length(user_dto.first_name) and self._has_valid_length(user_dto.last_name) and \
               self._has_valid_characters(user_dto.first_name) and self._has_valid_characters(user_dto.last_name)

    def _has_valid_length(self, value: str) -> bool:
        return len(value.strip()) >= 2

    def _has_valid_characters(self, value: str) -> bool:
        return value.isalpha() and bool(value.strip())
