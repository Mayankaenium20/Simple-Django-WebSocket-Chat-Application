from django.urls import re_path
from .import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]


#the websocket_urlpatterns list maps the WebSocket URL (ws/socket-server/) to the ChatConsumer class.