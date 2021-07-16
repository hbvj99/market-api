from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

from market.commons.socket_auth import CustomSocketAuthMiddleware
from market.notifications.api.v1.views.consumers import NotificationConsumer

ws_path = [
    path("notifications/", NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(  # Allow socket connections only from Allowed hosts
        CustomSocketAuthMiddleware(
            URLRouter(ws_path)
        ),
    ),
})
