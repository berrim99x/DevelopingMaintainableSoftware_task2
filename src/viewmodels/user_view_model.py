class UserViewModel:
    def __init__(self, first_name: str, last_name: str, success: bool = False, error_message: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.success = success
        self.error_message = error_message

    def to_dict(self):
        """ Convert ViewModel to a dictionary for UI interaction """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "success": self.success,
            "error_message": self.error_message
        }
