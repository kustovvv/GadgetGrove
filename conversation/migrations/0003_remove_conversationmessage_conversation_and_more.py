# Generated by Django 4.2.5 on 2023-11-09 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_conversationmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationmessage',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='conversationmessage',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='ConversationMessage',
        ),
    ]
