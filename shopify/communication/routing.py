# communication/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/conversation/(?P<conversation_pk>\d+)/$', consumers.MessageConsumer.as_asgi()),
]
