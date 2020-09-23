from django.contrib import admin
from .models import NoticeBoard, Tag


class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'contents',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tagname')


# Register your models here.
admin.site.register(NoticeBoard, NoticeBoardAdmin)
admin.site.register(Tag, TagAdmin)
