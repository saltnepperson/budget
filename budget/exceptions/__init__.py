from budget import app

class BudgetException(Exception):
    """Base class for all exceptions."""
    pass

class UserEmailAlreadyExists(BudgetException):

    def __init__(self, user_email):
        self.user_email = user_email
        app.logger.info(self)

    def __str__(self):
        return repr("User with email: {} already exists. Cannnot create"
                    " a user with this email.".format(self.user_email))