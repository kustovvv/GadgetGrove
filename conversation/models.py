from django.db import models
from django.utils import timezone

from item.models import Item
from authentication.models import User as CustomUser


def current_time():
    return timezone.now().time()


class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, related_name='conversation_members')
    created_by = models.ForeignKey(CustomUser, related_name='conversation_creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
        
    def __str__(self):
        return ", ".join([member.username for member in self.members.all()])


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.created_by} {self.created_at}'