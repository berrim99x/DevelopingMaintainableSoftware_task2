from src.ports.save_user_intput_port import SaveUserInputPort
from src.entities.user import User
from src.viewmodels.user_view_model import UserViewModel
from src.views.user_view import UserView

class UserController:
    def __init__(self, input_port: SaveUserInputPort):
        self.input_port = input_port

    def save_user(self, first_name: str, last_name: str):
        # إنشاء كائن User من البيانات المدخلة
        user = User(first_name, last_name)

        # تمرير المستخدم إلى Input Port لتنفيذ Use Case
        user_view_model = self.input_port.execute(user)

        # إنشاء View وتمرير ViewModel
        view = UserView(user_view_model)
        view.display_user()  # عرض النتيجة في الـ UI
