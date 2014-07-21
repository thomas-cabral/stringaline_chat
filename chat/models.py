from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Conversation(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    spawn = models.ForeignKey('self', related_name='spawns', blank=True, null=True, db_index=True)
    spawn_master = models.ForeignKey('self', related_name='s_master', blank=True, null=True, db_index=True)

    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Comments(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    conversation = models.ForeignKey(Conversation, related_name='conversation_comments', db_index=True)
    parentId = models.ForeignKey('Comments', related_name='parent_id', blank=True, null=True, db_index=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.body