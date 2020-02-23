from app import app
from flask import request, Response
from ..common import IncomingTextSchema, validate_api_payload, Messenger, PROCESS_TEXT_API, UserResponseSchema
from ..core.services import TextProcessing


@app.route(PROCESS_TEXT_API, methods=["POST"])
@validate_api_payload(IncomingTextSchema)
def text_processing(**kwargs):
    """This method is used to processing incoming text and give command accordingly"""

    if request.method == "POST":
        message = Messenger()
        message.text = kwargs.get('text')
        message.user_id = kwargs.get('user_id')
        text_helper = TextProcessing(message)
        text_helper.process_text()

        return Response(UserResponseSchema().dumps(message.response), mimetype="application/json")
