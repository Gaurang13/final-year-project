from functools import wraps
from flask import request, Response
from marshmallow.exceptions import ValidationError
from .schema import ErrorSchema
from ..common.errors import errors


def validate_api_payload(schema_class):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                schema = schema_class()
                payload = schema.dump(schema.load(request.json))
                kw = {**kw, **payload}
            except ValidationError as e:
                error = errors['BadRequestError']
                res = {'message': e.messages, 'error': error['error']}
                return Response(ErrorSchema().dumps(res), mimetype="application/json", status=error['status'])
            return f(*args, **kw)

        return wrapper

    return decorator



