import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MessageConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, message):
        await self.accept()

    async def websocket_receive(self, message):
        await self.send(text_data=json.dumps({
            'message': 'This is a message from the server!'
        }))

    async def websocket_disconnect(self, message):
        pass

    async def connect(self):
        self.conversation_pk = self.scope['url_route']['kwargs']['conversation_pk']
        self.room_group_name = f"conversation_{self.conversation_pk}"

        # Join the conversation group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the conversation group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        message = json.loads(text_data)
        sender = self.scope['user']
        content = message['content']

        # Save the message to the database (implement as needed)
        # ...

        # Broadcast the message to the conversation group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message_type': 'new_message',
                'message': content,
                'sender': sender.username,
                'timestamp': 'timestamp_placeholder',  # You'll need to replace this with the actual timestamp
            }
        )

    async def chat_message(self, event):
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message_type': event['message_type'],
            'message': event['message'],
            'sender': event['sender'],
            'timestamp': event['timestamp'],
        }))
