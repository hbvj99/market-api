import jwt
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from jwt import ExpiredSignatureError

from config.settings import SECRET_KEY

User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class CustomJWTAuthMiddleware:
    """
    Custom JWT verify middleware
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        decoded_header = [[word.decode() for word in sets] for sets in scope.get('headers')]
        if any('sec-websocket-protocol' in sublist for sublist in decoded_header) is False:
            return AnonymousUser()
        try:
            token = dict(decoded_header).get('sec-websocket-protocol')
            token_name = token.split(',')[0]
            token_key = token.split()[-1]
            if token_name == 'Token':
                jwt_decode = jwt.decode(token_key, SECRET_KEY, algorithms=['HS256'])
                user_id = jwt_decode['user_id']
                scope['user'] = await get_user(user_id)
            else:
                return AnonymousUser()
        except ExpiredSignatureError:
            scope['user'] = AnonymousUser()
        return await self.app(scope, receive, send)
