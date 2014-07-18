from rest_framework import serializers

from .models import Conversation, Comments


class RecursiveField(serializers.Serializer):
    def to_native(self, obj):
        return self.parent.to_native(obj)


class CommentsListSerializer(serializers.ModelSerializer):
    """
    Uses black magic to create up to 7 nested comments fully serialized
    """
    user = serializers.Field(source='user.username')
    parent_id = RecursiveField(many=True)

    class Meta:
        model = Comments
        fields = ('id', 'body', 'conversation', 'user', 'created_on', 'parent_id')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'body', 'conversation', 'user', 'created_on', 'parentId')

    user = serializers.Field(source='user.username')


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'body', 'user', 'comment_count', 'spawn', 'spawns',
                  'spawn_master', 's_master')

    user = serializers.Field(source='user.username')
    comment_count = serializers.Field(source='conversation_comments.count')


class ConversationCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'body', 'user')

    user = serializers.Field(source='user.username')
    #comments = CommentsSerializer(source='conversation_comments')