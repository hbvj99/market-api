from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

from market.commons.socket_auth import CustomJWTAuthMiddleware
from market.notifications.api.v1.views.consumers import NotificationConsumer

ws_path = [
    path("notifications/", NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(  # Allow socket connections only from Allowed hosts
        CustomJWTAuthMiddleware(
            URLRouter(ws_path)
        ),
    ),
})
