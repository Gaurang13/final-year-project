__all__ = ['errors']

errors = {
    'InternalServerException': {
        'ok': False,
        'error': 'SERVER_ERROR',
        'message': "Service is down. Please try again after some time!",
        'status': 500
    },
    'BadRequestError': {
        'ok': False,
        'error': 'BAD_REQUEST',
        'message': "",
        'status': 400
    }
}

