from unittest.mock import Mock
from abc import ABC, abstractmethod
from src.entities.user import User


def test_controller_calls_input_port():
    # Arrange
    spy_input_port = Mock(spec=SaveUserInputPort)
    controller = UserController(input_port=spy_input_port)

    # Act
    controller.save_user("Islam", "Hala")

    # Assert
    spy_input_port.execute.assert_called_once_with(User("Islam", "Hala"))
