from app.config.ExecutionCode import ExecutionCode
from app.core.exceptions import CustomException


class UserNotFoundException(CustomException):
    code = ExecutionCode.USER_NOT_FOUND
    error_code = ExecutionCode.USER_NOT_FOUND
    message = ExecutionCode.USER_NOT_FOUND.description