from app import app
from flask import request, Response
from ..common import validate_api_payload, UserSchema, Messenger, USER_API, UserResponseSchema
from ..core.services import UserHelper


@app.route(USER_API, methods=["POST"])
@validate_api_payload(UserSchema)
def create_user(**kwargs):
    """This api is used to create user"""
    if request.method == "POST":
        message = Messenger()
        message.first_name = kwargs.get('first_name')
        message.last_name = kwargs.get('last_name')
        message.email = kwargs.get('email')
        message.phone_number = kwargs.get('phone_number')

        user_helper = UserHelper(message)
        user_helper.create_user()

        return Response(UserResponseSchema().dumps(message.user_response), mimetype='application/json')