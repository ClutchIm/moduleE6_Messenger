from .models import *
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'username', 'image',]


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'members',]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'text', 'chat', 'date',]

