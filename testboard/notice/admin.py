from django.contrib import admin
from .models import NoticeBoard, Tag, TagListRelatedBoard


# Register your models here.
admin.site.register(NoticeBoard)
admin.site.register(Tag)
admin.site.register(TagListRelatedBoard)
