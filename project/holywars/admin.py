from django.contrib import admin

from holywars.models import Holywar, HolywarArgument, Thread, ThreadComments, ThreadCommentsLike, ThreadLike, Invite

admin.site.register(Holywar)
admin.site.register(HolywarArgument)
admin.site.register(Thread)

admin.site.register(ThreadCommentsLike)
admin.site.register(ThreadLike)

admin.site.register(Invite)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text', 'likes')

admin.site.register(ThreadComments, CommentsAdmin)
