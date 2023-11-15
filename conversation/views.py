from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, ConversationMessage


def conversations(request):
    if request.user.is_authenticated:
        option = 'conversations'
        conversations = Conversation.objects.filter(members=request.user)
        my_ads = request.GET.get('my_ads', '1')
        last_message = ''
        if conversations:
            if my_ads == '1':
                conversations = conversations.exclude(created_by=request.user)
            else:
                conversations = conversations.filter(created_by=request.user)

        context = {'option': option, 
                   'my_ads': my_ads,
                   'conversations': conversations,
                   }

        return render(request, 'conversation/conversations.html', context)
    else:
        return redirect('login')


def conversation(request, pk):
    if request.user.is_authenticated:
        conversation = get_object_or_404(Conversation, id=pk)
        messages = ConversationMessage.objects.filter(conversation=conversation)
        if len(messages) < 100:
            messages = messages[:100]
        else:
            messages = messages[len(messages)-100:]
        context = {'conversation': conversation,
                   'messages': messages,
                   }
        
        return render(request, 'conversation/conversation.html', context)
    else:
        return redirect('login')