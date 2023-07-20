"""
ASGI config for shopify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from communication.consumers import SocketConsumer, NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/socket/", SocketConsumer.as_asgi()),  # WebSocket route for SocketConsumer
        path("ws/notification/", NotificationConsumer.as_asgi()),  # WebSocket route for NotificationConsumer
    ]),
})
