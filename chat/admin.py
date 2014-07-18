from django.contrib import admin
from .models import Conversation, Comments
# Register your models here.


class CommentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comments, CommentsAdmin)


class ConversationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Conversation, ConversationAdmin)
