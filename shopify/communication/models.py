from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    member = models.ManyToManyField(User, related_name='conversations_as_member')
    sender = models.ForeignKey(User, related_name='conversations_as_sender', on_delete=models.CASCADE, default=1)
    modified_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp', '-modified_at')

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
