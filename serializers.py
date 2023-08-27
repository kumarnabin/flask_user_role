from marshmallow import Schema, fields


def user_serializer(user):
    return {
        'id': user.id,
        'username': user.username,
    }


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()


class RoleSchema(Schema):
    id = fields.Integer()
    name = fields.String()
