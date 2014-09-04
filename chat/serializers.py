from rest_framework import serializers

from .models import Conversation, Comments


class RecursiveField(serializers.Serializer):
    def to_native(self, obj):
        return self.parent.to_native(obj)


class CommentsListSerializer(serializers.ModelSerializer):
    body = serializers.CharField(required=True)
    user = serializers.Field(source='user')
    children = RecursiveField(many=True)

    class Meta:
        model = Comments
        fields = ('id', 'body', 'conversation', 'user', 'created_on', 'parent', 'children')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'body', 'conversation', 'user', 'created_on', 'parent')

    user = serializers.Field(source='user.username')


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'body', 'user', 'comment_count', 'spawn', 'spawns',
                  'spawn_master', 's_master')

    user = serializers.Field(source='user.username')
    comment_count = serializers.Field(source='conversation_comments.count')


class ConversationSimpleSpawn(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title')


class ConversationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'body', 'user', 'spawn', 'spawns', 'spawn_master')

    user = serializers.Field(source='user.username')
    spawn = ConversationSimpleSpawn(read_only=True)
    spawns = ConversationSimpleSpawn(many=True, read_only=True)
    spawn_master = ConversationSimpleSpawn(read_only=True)