from unittest.mock import Mock

import pytest

from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.entities.user import User
from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface

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
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)

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
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

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
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

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
    ]
)

def test_should_not_save_user_when_names_contain_only_spaces(user):
    user = User("   ", "   ")
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()
