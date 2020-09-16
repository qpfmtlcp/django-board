from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'contents', 'created','modified')

admin.site.register(Board, BoardAdmin)
