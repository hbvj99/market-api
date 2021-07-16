from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

from market.notifications.api.v1.views.consumers import NotificationConsumer

ws_path = [
    path("notifications/", NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(  # Allow socket connections only from Allowed hosts
        AuthMiddlewareStack(
            URLRouter(ws_path)
        ),
    ),
})
