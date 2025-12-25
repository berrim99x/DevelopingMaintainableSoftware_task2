from src.entities.user import User
from src.interface_adapters.gateways.user_repository import MySQLUserRepository
from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.ports.save_user_output_port import SaveUserOutputPort


mysql_user_repository = MySQLUserRepository(
    host="localhost",
    user="root",
    password="",
    database="user_db",
    port=3306
)

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
