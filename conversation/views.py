from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, ConversationMessage
from item.models import Item


def conversations(request):
    if request.user.is_authenticated:
        option = 'conversations'
        have_messages = False
        conversations = Conversation.objects.filter(members=request.user)
        if conversations:
            for conversation in conversations:
                if conversation.messages.all():
                    have_messages = True
                    break
        my_ads = request.GET.get('my_ads', '1')
        if conversations:
            if my_ads == '1':
                conversations = conversations.exclude(created_by=request.user)
            else:
                conversations = conversations.filter(created_by=request.user)

        context = {'option': option, 
                   'my_ads': my_ads,
                   'conversations': conversations,
                   'have_messages': have_messages
                   }

        return render(request, 'conversation/conversations.html', context)
    else:
        return redirect('login')


def conversation(request, item_id):
    if request.user.is_authenticated:
        item = Item.objects.get(id=item_id)
        try:
            conversation = Conversation.objects.get(item=item, members=request.user)
        
        except:
            conversation = Conversation()
            conversation.item = item
            conversation.created_by = request.user
            conversation.save()

            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

        try:
            messages = ConversationMessage.objects.filter(conversation=conversation)
            if len(messages) < 100:
                messages = messages[:100]
            else:
                messages = messages[len(messages)-100:]
        except:
            messages = ''
        
        context = {'conversation': conversation,
                   'messages': messages,
                   }
        
        return render(request, 'conversation/conversation.html', context)
    else:
        return redirect('login')