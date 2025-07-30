from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields

blp = Blueprint(
    "Auth",
    "auth",
    url_prefix="/auth",
    description="User authentication endpoints"
)

# Schemas for OpenAPI documentation
class RegisterSchema(Schema):
    username = fields.Str(required=True, description="Username")
    email = fields.Email(required=True, description="User email")
    password = fields.Str(required=True, description="Password")

class LoginSchema(Schema):
    email = fields.Email(required=True, description="User email")
    password = fields.Str(required=True, description="Password")

class AuthResponseSchema(Schema):
    access_token = fields.Str(description="JWT access token")
    user_id = fields.Int(description="User ID")


# PUBLIC_INTERFACE
@blp.route("/register")
class Register(MethodView):
    """Endpoint for registering a new user."""
    @blp.arguments(RegisterSchema, location='json')
    @blp.response(201, AuthResponseSchema)
    def post(self, data):
        """
        Register a new user.
        ---
        summary: Register new user
        description: Registers a user and returns an access token.
        """
        # Placeholder implementation
        return {"access_token": "token", "user_id": 1}, 201


# PUBLIC_INTERFACE
@blp.route("/login")
class Login(MethodView):
    """Endpoint for user login."""
    @blp.arguments(LoginSchema, location='json')
    @blp.response(200, AuthResponseSchema)
    def post(self, data):
        """
        Authenticate user and return an access token.
        ---
        summary: User login
        description: Authenticates user and returns an access token.
        """
        # Placeholder implementation
        return {"access_token": "token", "user_id": 1}, 200
