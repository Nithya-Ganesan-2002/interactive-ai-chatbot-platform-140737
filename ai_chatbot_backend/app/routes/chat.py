from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields

blp = Blueprint(
    "Chat",
    "chat",
    url_prefix="/chat",
    description="Chat message endpoints"
)

class SendMessageSchema(Schema):
    message = fields.Str(required=True, description="Message to send")

class MessageResponseSchema(Schema):
    message_id = fields.Int(description="ID of the message")
    sender = fields.Str(description="Sender identifier")
    content = fields.Str(description="Message content")
    timestamp = fields.Str(description="Timestamp of message")

class ChatHistoryResponseSchema(Schema):
    history = fields.List(fields.Nested(MessageResponseSchema), description="Chat history")

# PUBLIC_INTERFACE
@blp.route("/send")
class SendMessage(MethodView):
    """Send a chat message."""
    @blp.arguments(SendMessageSchema, location="json")
    @blp.response(200, MessageResponseSchema)
    def post(self, data):
        """
        Send a chat message and get response.
        ---
        summary: Send message
        description: Send a chat message, receive AI response.
        """
        # Placeholder response
        return {
            "message_id": 123,
            "sender": "user",
            "content": data["message"],
            "timestamp": "2024-01-01T00:00:00Z"
        }

# PUBLIC_INTERFACE
@blp.route("/history")
class ChatHistory(MethodView):
    """Get chat history."""
    @blp.response(200, ChatHistoryResponseSchema)
    def get(self):
        """
        Retrieve chat history for user.
        ---
        summary: Get chat history
        description: Returns list of previous messages.
        """
        return {
            "history": [
                {
                    "message_id": 1,
                    "sender": "user",
                    "content": "Hello",
                    "timestamp": "2024-01-01T00:00:00Z"
                },
                {
                    "message_id": 2,
                    "sender": "AI",
                    "content": "Hi, how can I help you?",
                    "timestamp": "2024-01-01T00:00:01Z"
                }
            ]
        }
