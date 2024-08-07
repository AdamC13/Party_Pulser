from marshmallow import fields
from . import ma

class UserSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    username = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    age = fields.String(required=True)
    password = fields.String(required=True)
    picture_path = fields.String(required=True)

    class Meta:
        fields = ("id", "username", "email", "phone", "age", "password", 'picture_path')

user_input_schema = UserSchema()
