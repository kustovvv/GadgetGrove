import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import ConversationMessage, Conversation
from account.models import CustomUser

from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.conversation_group_id = 'chat_%s' % self.conversation_id

        await self.channel_layer.group_add(
            self.conversation_group_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.conversation_group_id,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        conversation_id = data['conversation_id']

        await self.save_message(username, conversation_id, message)

        await self.channel_layer.group_send(
            self.conversation_group_id,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'conversation_id': conversation_id
            }
        )
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        conversation_id = event['conversation_id']
        created_at = datetime.now()

        created_at_str = created_at.strftime("%b. %d, %Y, %I:%M %p").replace("AM", "a.m.").replace("PM", "p.m.").replace(" 0", " ")

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'conversation_id': conversation_id,
            'created_at': created_at_str
        }))

    @sync_to_async
    def save_message(self, username, conversation_id, message):
        user = CustomUser.objects.get(username=username)
        conversation = Conversation.objects.get(id=conversation_id)

        ConversationMessage.objects.create(conversation=conversation, created_by=user, content=message)
        