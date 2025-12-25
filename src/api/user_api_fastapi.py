from fastapi import FastAPI
from pydantic import BaseModel
from src.entities.user_dto import UserDTO
from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.ports.save_user_output_port import SaveUserOutputPort

app = FastAPI()


class ConsolePresenter(SaveUserOutputPort):
    def present_success(self):
        print("User successfully saved!")

    def present_error(self, message: str):
        print(f"Error: {message}")

presenter = ConsolePresenter()

class User(BaseModel):
    first_name: str
    last_name: str

@app.post("/save_user")
async def save_user(user: User):
        user_dto = UserDTO(first_name=user.first_name, last_name=user.last_name)
        user_view_model = saving_use_case.execute(user_dto)

        if user_view_model.success:
            return {"message": f"User {user_view_model.first_name} saved successfully!"}
        else:
            return {"error": user_view_model.error_message}, 400
