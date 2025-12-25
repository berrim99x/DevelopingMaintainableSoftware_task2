from abc import ABC, abstractmethod

from src.entities.user import User


class SaveUserInputPort(ABC):
    @abstractmethod
    def execute(self, user: User) -> None:
        pass
