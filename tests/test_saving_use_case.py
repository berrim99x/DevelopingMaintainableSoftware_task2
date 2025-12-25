from unittest.mock import Mock
import pytest

from src.entities.user_dto import UserDTO
from src.interface_adapters.gateways.user_repository import MySQLUserRepository
from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.entities.user import User
from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.ports.save_user_output_port import SaveUserOutputPort

@pytest.mark.parametrize(
    "user",
    [
        User("Islam", "Hala"),
        User("Abdelhakim", "Berrim"),
        User("Dhia", "Okba"),
        User("Adam", "Hibi"),
        User("Oussama", "Khelef"),
        User("Ahmed", "Zellouma"),
    ])
def test_saving_user_is_calling_delegated_repository(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)  # Mocking the presenter
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)
    spy_presenter.present_success.assert_called_once()

@pytest.mark.parametrize(
    "user",
    [
        User("", "Hala"),
        User("", "Berrim"),
        User("", "Okba"),
        User("", "Hibi"),
        User("", "Khelef"),
        User("", "Zellouma"),
    ])
def test_should_not_save_user_when_first_name_is_empty(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()

@pytest.mark.parametrize(
    "user",
    [
        User("Islam", ""),
        User("Abdelhakim", ""),
        User("Dhia", ""),
        User("Adam", ""),
        User("Oussama", ""),
        User("Ahmed", ""),
    ])
def test_should_not_save_user_when_last_name_is_empty(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()

@pytest.mark.parametrize(
    "user",
    [
        User(" ", " "),
        User("", ""),
        User("", "   "),
        User("   ", ""),
    ])
def test_should_not_save_user_when_names_contain_only_spaces(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()

@pytest.mark.parametrize(
    "user",
    [
        User("I", "Hal"),
        User("A", "Berrim"),
        User("D", "Okba"),
    ])
def test_should_not_save_user_when_first_name_is_too_short(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()

@pytest.mark.parametrize(
    "user",
    [
        User("Islam", "H"),
        User("Abdelhakim", "B"),
        User("Dhia", "O"),
    ])
def test_should_not_save_user_when_last_name_is_too_short(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()

@pytest.mark.parametrize(
    "user",
    [
        User("I4556@slam", "Hala"),
        User("Abdel--(hakim", "Berrim"),
        User("Dhi0.a", "Okba"),
    ])
def test_should_not_save_user_when_first_name_contains_symbols(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()

@pytest.mark.parametrize(
    "user",
    [
        User("Islam", "H1313"),
        User("Abdelhakim", "-_è"),
        User("Dhia", "Oé&'"),
    ])
def test_should_not_save_user_when_last_name_contains_numbers(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()

def test_save_user_integration():
    # Arrange
    spy_user_repository = Mock(spec=MySQLUserRepository)
    spy_presenter = Mock(spec=SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    user_dto = UserDTO("Islam", "Hala")

    # Act
    saving_use_case.execute(user_dto)

    # Assert
    spy_user_repository.save.assert_called_once_with(user_dto)
    spy_presenter.present_success.assert_called_once()  # التأكد من استدعاء present_success