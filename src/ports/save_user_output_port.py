from abc import ABC, abstractmethod

class SaveUserOutputPort(ABC):
    @abstractmethod
    def present_success(self):
        pass

    @abstractmethod
    def present_error(self, message: str):
        pass
