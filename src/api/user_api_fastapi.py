from fastapi import FastAPI
from pydantic import BaseModel
from src.entities.user_dto import UserDTO
from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.ports.save_user_output_port import SaveUserOutputPort
from unittest.mock import Mock

app = FastAPI()

# محاكاة MySQLUserRepository باستخدام Mock
class MockUserRepository:
    def save(self, user_dto: UserDTO) -> None:
        print(f"Mock: User {user_dto.first_name} {user_dto.last_name} saved to Mock database.")

# محاكاة Presenter (SaveUserOutputPort)
class ConsolePresenter(SaveUserOutputPort):
    def present_success(self):
        print("User successfully saved!")

    def present_error(self, message: str):
        print(f"Error: {message}")

# إعداد SaveUseCase باستخدام Mock
mock_user_repository = MockUserRepository()
presenter = ConsolePresenter()
saving_use_case = SavingUseCase(user_repository=mock_user_repository, presenter=presenter)

class User(BaseModel):
    first_name: str
    last_name: str

@app.post("/save_user")
async def save_user(user: User):
    try:
        print(f"Received user: {user.first_name} {user.last_name}")  # Debugging output
        user_dto = UserDTO(first_name=user.first_name, last_name=user.last_name)
        user_view_model = saving_use_case.execute(user_dto)

        if user_view_model.success:
            return {"message": f"User {user_view_model.first_name} saved successfully!"}
        else:
            return {"error": user_view_model.error_message}, 400
    except Exception as e:
        print(f"Error occurred: {e}")  # Debugging output
        return {"error": "Internal Server Error"}, 500
