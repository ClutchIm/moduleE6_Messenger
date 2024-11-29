from django.shortcuts import render
from rest_framework import viewsets
import django_filters

from .models import *
from .serializers import *

# Create your views here.

def index(request):
    members = Member.objects.all()
    chats = Chat.objects.all()
    messages = Message.objects.all()

    return render(
        request,
        'index.html',
        {'members': members, 'chats': chats, 'messages': messages}
    )


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_queryset(self):
        queryset = self.queryset
        member_id = self.request.query_params.get('member_id', None)
        chat_id = self.request.query_params.get('chat_id', None)
        if member_id is not None:
            queryset = queryset.filter(chat__members_id=member_id)
        if chat_id is not None:
            queryset = queryset.filter(chat_id=chat_id)
        return queryset



class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
