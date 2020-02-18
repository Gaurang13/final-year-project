from app import app
from .exception import BlindEyeException
from flask import Response
from .schema import ErrorSchema


@app.errorhandler(BlindEyeException)
def handle_exception(err):
    """ Global exception handler."""

    return Response(ErrorSchema().dumps(err.error), mimetype="application/json")

