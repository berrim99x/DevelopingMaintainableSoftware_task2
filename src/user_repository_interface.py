from abc import ABCMeta, abstractmethod

from src.user import User


class UserRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User) -> None:
        pass
