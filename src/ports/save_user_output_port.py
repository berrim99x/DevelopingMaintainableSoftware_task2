class SaveUserOutputPort:
    def present_success(self):
        raise NotImplementedError

    def present_error(self, message: str):
        raise NotImplementedError
