from builtins import Exception


class BlindEyeException(Exception):
    pass


class BadRequestError(BlindEyeException):
    def __init__(self, error):
        self.error = error