from unittest.mock import Mock

from src.controller.user_controller import UserController
from src.entities.user import User
from src.ports.save_user_intput_port import SaveUserInputPort
from src.viewmodels.user_view_model import UserViewModel
from src.views.user_view import UserView


def test_controller_calls_input_port():
    # Arrange
    spy_input_port = Mock(spec=SaveUserInputPort)
    controller = UserController(input_port=spy_input_port)

    # Act
    controller.save_user("Islam", "Hala")

    # Assert
    spy_input_port.execute.assert_called_once_with(User("Islam", "Hala"))


def test_user_view_display():
    # Arrange
    user_view_model = UserViewModel("Islam", "Hala", success=True)
    user_view = UserView(user_view_model)

    # Act
    result = user_view.display_user()  # هذا يعيد النص بدلاً من طباعته

    # Assert
    # نتحقق من أن الرسالة التي تم عرضها تحتوي على "saved successfully"
    assert "saved successfully" in result
