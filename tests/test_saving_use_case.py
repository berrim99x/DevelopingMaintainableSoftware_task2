from unittest.mock import Mock

import pytest

from src.saving_use_case import SavingUseCase
from src.user import User
from src.user_repository_interface import UserRepositoryInterface

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
    user = User(first_name="Islam", last_name="Hala")
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)


def test_should_not_save_user_when_first_name_is_empty():
    # Arrange
    user = User(first_name="", last_name="Hala")
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_not_called()