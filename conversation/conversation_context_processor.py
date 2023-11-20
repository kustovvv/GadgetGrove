from .models import Conversation


def conversations_data(request):
    conversations = Conversation.objects.filter(members=request.user)
    return {'conversations': conversations}