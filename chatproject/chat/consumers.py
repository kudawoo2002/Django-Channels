from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message, UserChannel
from django.contrib.auth.models import User
import json
from datetime import datetime


class chatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # print(self.channel_name)

        self.person_id = self.scope.get("url_route").get("kwargs").get("id")
        user_channel = UserChannel()
        try:
            user_channel = UserChannel.objects.get(user=self.scope.get("user"))
            user_channel.channel_name = self.channel_name
            user_channel.save()

        except:
            
             user_channel.user = self.scope.get("user")
             user_channel.channel_name = self.channel_name
             user_channel.save()
        

    
    def receive(self, text_data):
        text_data = json.loads(text_data)
        # print(text_data.get("type"))
        # print(text_data.get("message"))
        now = datetime.now()
        date = now.date()
        time = now.time()

        other_user = User.objects.get(id=self.person_id)
        new_message = Message()
        new_message.from_who = self.scope.get("user")
        new_message.to_who = other_user
        new_message.message = text_data.get("message")
        new_message.date = date
        new_message.time = time
        new_message.has_been_seen = False
        new_message.save()
        
        try:
            user_channel_name = UserChannel.objects.get(user=other_user)
            data = {
                "type":"receiver_function",
                "type_of_message":"new_message",
                "data": text_data.get("message")
            }

            async_to_sync(self.channel_layer.send)(user_channel_name.channel_name, data)
        except:
            pass


    def receiver_function(self, what_you_send):
        data = json.dumps(what_you_send)
        self.send(data)