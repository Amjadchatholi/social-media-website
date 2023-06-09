from user.serializers import UserSerializer, ChatUserSerializer
from .models import Conversation, Chat, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('conversation_id',)


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = UserSerializer()
    receiver = UserSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'last_message']

    def get_last_message(self, instance):
        message = instance.message_set.first()
        return MessageSerializer(instance=message)


class ConversationSerializer(serializers.ModelSerializer):
    initiator = ChatUserSerializer()
    receiver = ChatUserSerializer()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'message_set']



class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Chat
        fields = ('id', 'created', 'message', 'sender')