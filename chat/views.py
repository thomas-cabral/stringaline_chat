from django.views import generic
from rest_framework import generics, permissions

from .serializers import CommentsSerializer, ConversationSerializer, ConversationCommentsSerializer,\
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
    queryset = Conversation.objects.all().select_related('user')
    serializer_class = ConversationCommentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


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
        """
        prefect_related up to 7 layers of comments
        reduces queries by 1 per nested comment at each level
        :return:
        """
        comments = Comments.objects.filter(conversation=self.kwargs['pk'], parentId__isnull=True)\
            .select_related('user').prefetch_related('parent_id__parent_id__parent_id__parent_id__parent_id'
                                                     '__parent_id__parent_id')
        return comments


class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'


class AngularConversationList(generic.TemplateView):
    template_name = 'chat/conversation_list.html'


class AngularConversationDetail(generic.TemplateView):
    template_name = 'chat/conversation_detail.html'