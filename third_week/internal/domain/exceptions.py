class ApiError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return self.message

    def get_status_code(self):
        return self.status_code

    def get_error(self):
        data_error = {
            "status_code": self.get_status_code(),
            "detail": f"{type(self).__name__}: {self}",
        }

        return data_error
    
class IncorrectData(ApiError):
    def __init__(self):
        __status_code = 400
        __message = f"Incorrect data"

        super().__init__(__status_code, __message)

class IncorrectName(ApiError):
    def __init__(self, quantity):
        self.quantity = quantity

        __status_code = 400
        __message = f"The name must contain at least {self.quantity} characters"

        super().__init__(__status_code, __message)

class IncorrectPassword(ApiError):    
    def __init__(self, quantity):
        self.quantity = quantity

        __status_code = 400
        __message = f"The password must contain at least {self.quantity} characters"

        super().__init__(__status_code, __message)

class UserNotFound(ApiError):   
    def __init__(self):
        __status_code = 401
        __message = f"Incorrect login or password"

        super().__init__(__status_code, __message)

class InvalidToken(ApiError):    
    def __init__(self):
        __status_code = 401
        __message = f"InvalidToken"

        super().__init__(__status_code, __message)

class InsufficientRights(ApiError):    
    def __init__(self):
        __status_code = 401
        __message = f"InsufficientRights"

        super().__init__(__status_code, __message)