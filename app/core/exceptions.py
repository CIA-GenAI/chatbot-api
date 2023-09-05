from http import HTTPStatus
from fastapi import HTTPException

class CustomException(Exception):
    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, message=None):
        if message:
            self.message = message

class CustomHttpException(HTTPException):
    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, message=None):
        if message:
            self.message = message
        super().__init__(status_code = self.code, detail = self.message)


class BadRequestException(CustomHttpException):
    code = HTTPStatus.BAD_REQUEST
    error_code = HTTPStatus.BAD_REQUEST
    message = HTTPStatus.BAD_REQUEST.description


class NotFoundException(CustomHttpException):
    code = HTTPStatus.NOT_FOUND
    error_code = HTTPStatus.NOT_FOUND
    message = HTTPStatus.NOT_FOUND.description


class ForbiddenException(CustomHttpException):
    code = HTTPStatus.FORBIDDEN
    error_code = HTTPStatus.FORBIDDEN
    message = HTTPStatus.FORBIDDEN.description


class UnauthorizedException(CustomHttpException):
    code = HTTPStatus.UNAUTHORIZED
    error_code = HTTPStatus.UNAUTHORIZED
    message = HTTPStatus.UNAUTHORIZED.description


class UnprocessableEntity(CustomException):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description


class DuplicateValueException(CustomException):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description
    

