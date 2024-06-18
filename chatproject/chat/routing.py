from django.urls import path
from . import consumers

ASGI_urlpatterns = [
    path("websocket/<int:id>", consumers.chatConsumer.as_asgi())
]