from django.contrib import admin
from .models import Board, History


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'contents', 'owner')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')


admin.site.register(Board, BoardAdmin)
admin.site.register(History, HistoryAdmin)
