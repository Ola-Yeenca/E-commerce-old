import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Process the received message and send a response if needed
        # You can handle different types of messages and implement the logic accordingly
        await self.send(text_data=json.dumps({
            'message': 'Your response message here'
        }))

        
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Handle the incoming message, if needed
        # You can use the received data to update the inbox or show notifications
        # For example, you can broadcast a new message to all connected clients:
        await self.send(text_data=json.dumps({
            'message': 'You have a new message!'
        }))
