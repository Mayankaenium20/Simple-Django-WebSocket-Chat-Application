import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'               #name of the group for the given chatroom
        async_to_sync(self.channel_layer.group_add)(            #adds the websocket connection to the specific group and layers
            self.room_group_name,                               
            self.channel_name   
        )
        self.accept()                                           #initiates the socket connection for further com

        # wraps an asynchronous function (or coroutine) and converts it into a synchronous function - read async_sync.md

    def receive(self, text_data):                                   #handles tasks when the user begins to chat
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        user = text_data_json.get('user', 'Anonymous')                  #message, user defined in a variable

        async_to_sync(self.channel_layer.group_send)(                   #send the above msg to all the members in the group containing multiple layers
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user
            }
        )

    def chat_message(self, event):
        message = event['message']
        user = event['user']
        self.send(text_data=json.dumps({                        #based on the defined event, the data is sent back to group with the type, message, and the user.
            'type': 'chat',
            'message': message,
            'user': user
        }))

    def disconnect(self, close_code):
        pass

