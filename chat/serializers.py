from rest_framework import serializers

from .models import Conversation, Comments


class CommentsListSerializer(serializers.ModelSerializer):
    """
    Uses black magic to create up to 7 nested comments fully serialized
    """
    class Meta:
        model = Comments
        fields = ('id', 'body', 'conversation', 'user', 'created_on', 'parent_id')

    user = serializers.Field(source='user.username')

CommentsListSerializer.base_fields['parent_id'] = CommentsListSerializer(many=True)
CommentsListSerializer.base_fields['parent_id'] = CommentsListSerializer(many=True)
CommentsListSerializer.base_fields['parent_id'] = CommentsListSerializer(many=True)
CommentsListSerializer.base_fields['parent_id'] = CommentsListSerializer(many=True)
CommentsListSerializer.base_fields['parent_id'] = CommentsListSerializer(many=True)
CommentsListSerializer.base_fields['parent_id'] = CommentsListSerializer(many=True)
CommentsListSerializer.base_fields['parent_id'] = CommentsListSerializer(many=True)


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