from unittest.mock import Mock

from src.controller.user_controller import UserController
from src.entities.user import User
from src.ports.save_user_intput_port import SaveUserInputPort


def test_controller_calls_input_port():
    # Arrange
    spy_input_port = Mock(spec=SaveUserInputPort)
    controller = UserController(input_port=spy_input_port)

    # Act
    controller.save_user("Islam", "Hala")

    # Assert
    spy_input_port.execute.assert_called_once_with(User("Islam", "Hala"))


