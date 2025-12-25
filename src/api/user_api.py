from flask import Flask, request, jsonify
from src.entities.user_dto import UserDTO
from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.interface_adapters.gateways.user_repository import MySQLUserRepository
from src.ports.save_user_output_port import SaveUserOutputPort

app = Flask(__name__)

# إعداد MySQLUserRepository
user_repository = MySQLUserRepository(
    host="localhost", user="root", password="password", database="user_db"
)

# إعداد Presenter (SaveUserOutputPort)
class ConsolePresenter(SaveUserOutputPort):
    def present_success(self):
        print("User successfully saved!")

    def present_error(self, message: str):
        print(f"Error: {message}")

presenter = ConsolePresenter()

# إعداد SaveUseCase
saving_use_case = SavingUseCase(user_repository=user_repository, presenter=presenter)

@app.route("/save_user", methods=["POST"])
def save_user():
    data = request.get_json()
    user_dto = UserDTO(first_name=data["first_name"], last_name=data["last_name"])

    # تنفيذ Use Case
    user_view_model = saving_use_case.execute(user_dto)

    # إعادة النتيجة على شكل JSON
    if user_view_model.success:
        return jsonify({"message": f"User {user_view_model.first_name} saved successfully!"}), 200
    else:
        return jsonify({"error": user_view_model.error_message}), 400


if __name__ == "__main__":
    app.run(debug=True)
