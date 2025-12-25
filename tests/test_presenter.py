from unittest.mock import Mock
import pytest

from src.entities.user import User
from src.ports.save_user_output_port import SaveUserOutputPort
from src.use_cases.saving_user.saving_use_case import SavingUseCase

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
def test_presenter_is_called_when_user_is_saved(user):
    # Arrange
    spy_user_repository = Mock()
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_presenter.present_success.assert_called_once()

@pytest.mark.parametrize(
    "user",
    [
        User("", "Hala"),
        User("@gfg", "Berrim"),
        User("", ""),
        User("", "Hibi12"),
        User("", "Khelef"),
        User(")", "Zellouma"),
    ])
def test_presenter_is_called_when_user_data_is_invalid(user):
    # Arrange
    spy_user_repository = Mock()
    spy_presenter = Mock(SaveUserOutputPort)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository, presenter=spy_presenter)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_presenter.present_error.assert_called_once_with("Invalid user data")
