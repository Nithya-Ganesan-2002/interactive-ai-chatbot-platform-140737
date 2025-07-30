from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields

blp = Blueprint(
    "Users",
    "users",
    url_prefix="/users",
    description="User profile management endpoints"
)

class UserProfileSchema(Schema):
    user_id = fields.Int(description="User ID")
    username = fields.Str(description="Username")
    email = fields.Email(description="User email")

class UpdateProfileSchema(Schema):
    username = fields.Str(description="New username")
    email = fields.Email(description="New email")

# PUBLIC_INTERFACE
@blp.route("/me")
class UserProfile(MethodView):
    """Get the current user's profile."""
    @blp.response(200, UserProfileSchema)
    def get(self):
        """
        Retrieve profile information for current user.
        ---
        summary: Get user profile
        description: Returns profile info of the current user.
        """
        # Placeholder response
        return {
            "user_id": 1,
            "username": "demo_user",
            "email": "demo@example.com"
        }

    @blp.arguments(UpdateProfileSchema, location="json")
    @blp.response(200, UserProfileSchema)
    def put(self, data):
        """
        Update profile info for current user.
        ---
        summary: Update user profile
        description: Updates and returns user profile information.
        """
        # Placeholder response
        return {
            "user_id": 1,
            "username": data.get("username", "demo_user"),
            "email": data.get("email", "demo@example.com")
        }
