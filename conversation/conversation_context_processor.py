from .models import Conversation


def conversations_data(request):
    if request.user.is_authenticated:
        conversations = Conversation.objects.filter(members=request.user)
    else:
        conversations = '0'
    return {'conversations': conversations}