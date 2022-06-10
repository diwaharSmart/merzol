import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import socket_server.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "merzol.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            socket_server.routing.websocket_urlpatterns
        )
    ),
})