from src.user import User
from src.user_repository_interface import UserRepositoryInterface


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, user: User) -> None:
        self.user_repository.save(user)
