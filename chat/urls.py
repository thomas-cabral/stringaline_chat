from django.conf.urls import url, patterns
from . import views

apiurls = patterns('',
    url(r'^api/conversation/$', views.ConversationList.as_view()),
    url(r'^api/conversation/(?P<pk>[0-9]+)/$', views.ConversationDetail.as_view()),
    url(r'^api/conversation/(?P<pk>[0-9]+)/comments/$', views.CommentConversationList.as_view()),
    url(r'^api/comment/$', views.CommentsList.as_view()),
)

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),
    url(r'^angular/conversation-list/$', views.AngularConversationList.as_view()),
    url(r'^angular/conversation-detail/$', views.AngularConversationDetail.as_view()),
) + apiurls