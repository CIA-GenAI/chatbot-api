from app.core.exceptions import CustomException, CustomHttpException
from app.config.ExecutionCode import ExecutionCode


class PasswordDoesNotMatchException(CustomException):
    code = 401
    error_code = 20000
    message = "password does not match"


class DuplicateEmailOrNicknameException(CustomException):
    code = 400
    error_code = 20001
    message = "duplicate email or nickname"


class CredentialsNotFoundException(CustomException):
    code = 404
    error_code = 20002
    message = "user not found"
    
class DecodeTokenException(CustomException):
    code = 400
    error_code = 10000
    message = "token decode error"


class ExpiredTokenException(CustomHttpException):
    code = 400
    error_code = 10001
    message = "expired token"

class CredentialsNotFoundException(CustomHttpException):
    code = ExecutionCode.CREDENTIALS_NOT_FOUND
    error_code = ExecutionCode.CREDENTIALS_NOT_FOUND
    message = ExecutionCode.CREDENTIALS_NOT_FOUND.description