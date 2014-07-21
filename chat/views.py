from django.views import generic
from rest_framework import generics, permissions

from .serializers import CommentsSerializer, ConversationSerializer, ConversationDetailSerializer, \
    CommentsListSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Conversation, Comments


class ConversationList(generics.ListCreateAPIView):
    queryset = Conversation.objects.all().select_related('user')\
        .prefetch_related('conversation_comments', 's_master', 'spawns')\
        .order_by('-created_on')
    serializer_class = ConversationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class ConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConversationDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_queryset(self):
        conversation = Conversation.objects.filter(pk=self.kwargs['pk'], ).select_related('user')\
            .prefetch_related('conversation_comments', 's_master', 'spawns')
        return conversation


class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all().select_related('user')
    serializer_class = CommentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class CommentConversationList(generics.ListAPIView):
    serializer_class = CommentsListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        comments = Comments.objects.filter(conversation=self.kwargs['pk'], parentId__isnull=True)
        c = comments.select_related().prefetch_related('parent_id')

        return c


class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'


class AngularConversationList(generic.TemplateView):
    template_name = 'chat/conversation_list.html'


class AngularConversationDetail(generic.TemplateView):
    template_name = 'chat/conversation_detail.html'