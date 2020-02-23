from marshmallow import Schema, fields, validate, pre_load, validates, ValidationError
import re


class ErrorSchema(Schema):
    ok = fields.Boolean(default=False)
    error = fields.String(default='INTERNAL_SERVER')
    message = fields.Raw()
    status = fields.String()


class IncomingTextSchema(Schema):
    text = fields.String(required=True, validate=validate.Length(min=1))
    user_id = fields.Int(required=True, min=1)


class UserSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    email = fields.String(required=True, validate=validate.Length(min=1, max=50))
    password = fields.String(required=True, validate=validate.Length(min=1, max=50))
    phone_number = fields.String(required=True, validate=validate.Length(min=10, max=15))

    @validates('email')
    def validate_email(self, value):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex, value):
            raise ValidationError("Please enter valid email address")


class UserResponseSchema(Schema):
    user_id = fields.Int()
    text_id = fields.Int()
    text = fields.String()
    ok = fields.Boolean(default=True)
    status = fields.String()

