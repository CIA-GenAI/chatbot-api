from enum import IntEnum

class ExecutionCode(IntEnum):
    def __new__(cls, value, phrase, description=''):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        obj.description = description
        return obj

    ###################################
    #  General pogram execution code  #
    ###################################
    PROCESSING = 102, 'Processing'
    EXIT = (0, 'Exit', 'Normal exit')
    EXIT_ERROR = (0, 'Exit', 'Erro exit')

    # auth module
    AUTH_INVALID = (100404, 'Invalid credentials',
            'Credentials provided are invalid')
    CREDENTIALS_NOT_FOUND = (102404, 'Credentials not found',
            'Credentials not found')
    
    # user module
    USER_NOT_FOUND = 200404, 'User not found', 'Request received, please continue'


