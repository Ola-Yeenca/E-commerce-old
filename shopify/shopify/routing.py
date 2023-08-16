from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from communication.consumers import SocketConsumer
from communication.consumers import NotificationConsumer
from communication.consumers import MessageConsumer

from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/socket/", SocketConsumer.as_asgi()),
            path("ws/notification/", NotificationConsumer.as_asgi()),
            path("ws/conversation/(?P<conversation_pk>\d+)/$", MessageConsumer.as_asgi()),
        ]),
    ),
})
