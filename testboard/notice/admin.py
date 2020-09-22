from django.contrib import admin
from .models import NoticeBoard


class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'contents')


# Register your models here.
admin.site.register(NoticeBoard, NoticeBoardAdmin)
