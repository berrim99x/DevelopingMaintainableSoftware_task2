class UserView:
    def __init__(self, view_model):
        self.view_model = view_model

    def display_user(self):
        """ عرض النتيجة في الـ UI """
        if self.view_model.success:
            return f"User {self.view_model.first_name} {self.view_model.last_name} saved successfully!"
        else:
            return f"Error: {self.view_model.error_message}"
