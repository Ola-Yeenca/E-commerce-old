from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from communication.consumers import SocketConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", SocketConsumer.as_asgi()),
    ]),
})
