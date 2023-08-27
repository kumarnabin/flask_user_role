from marshmallow import Schema, fields


def user_serializer(user):
    return {
        'id': user.id,
        'username': user.username,
        'roles': RoleSchema(many=True).dump(user.roles),
    }


class RoleSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    roles = fields.Nested(RoleSchema(), many=True)