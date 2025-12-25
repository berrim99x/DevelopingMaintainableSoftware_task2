from src.entities.user import User
from src.interface_adapters.gateways.user_repository import MySQLUserRepository
from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.ports.save_user_output_port import SaveUserOutputPort

# إعداد MySQLUserRepository مع تفاصيل الاتصال
# تأكد من تحديد المنفذ الصحيح إذا كان مختلفًا عن 3306
mysql_user_repository = MySQLUserRepository(
    host="localhost",
    user="root",
    password="",  # تأكد من تركها فارغة إذا لم يكن لديك كلمة مرور
    database="user_db",  # اسم قاعدة البيانات
    port=3306  # تأكد من أن المنفذ هنا هو المنفذ الصحيح
)

# إعداد Presenter (Output Port)
class ConsolePresenter(SaveUserOutputPort):
    def present_success(self):
        print("User successfully saved!")

    def present_error(self, message: str):
        print(f"Error: {message}")

# إعداد UseCase
presenter = ConsolePresenter()
saving_use_case = SavingUseCase(user_repository=mysql_user_repository, presenter=presenter)

# تنفيذ SaveUserUseCase
user = User(first_name="Abdelhakim", last_name="Berrim")
saving_use_case.execute(user)
