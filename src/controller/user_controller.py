from src.entities.user import User
from src.ports.save_user_intput_port import SaveUserInputPort


class UserController:
    def __init__(self, input_port: SaveUserInputPort):
        self.input_port = input_port

    def save_user(self, first_name: str, last_name: str):
        # إنشاء كائن User من البيانات المدخلة
        user = User(first_name, last_name)

        # تمرير المستخدم إلى Input Port لتنفيذ Use Case
        self.input_port.execute(user)
