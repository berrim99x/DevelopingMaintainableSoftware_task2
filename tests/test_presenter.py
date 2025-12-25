from unittest.mock import Mock
import pytest

from src.entities.user import User
from src.ports.save_user_output_port import SaveUserOutputPort
from src.use_cases.saving_user.saving_use_case import SavingUseCase


def test_presenter_is_called_when_user_is_saved():
    # Arrange
    user = User("Islam", "Hala")  # بيانات صحيحة
    spy_user_repository = Mock()
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_presenter.present_success.assert_called_once()

def test_presenter_is_called_when_user_data_is_invalid():
    # Arrange
    user = User("", "Hala")
    spy_user_repository = Mock()
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_presenter.present_error.assert_called_once_with("Invalid user data")
