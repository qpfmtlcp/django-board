from django.contrib import admin
from .models import Board, History, Tag


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'contents', 'owner')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tagname')

admin.site.register(Board, BoardAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Tag, TagAdmin)
