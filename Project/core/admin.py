from django.contrib import admin

from .models import Member, Chat, Message


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('id', 'username', 'image')


class ChatAdmin(admin.ModelAdmin):
    model = Chat
    list_display = ('id', 'name')


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'chat', 'author', 'text', 'date')


admin.site.register(Member, MemberAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
