from django.contrib import admin
from .models import board

class boardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'contents', 'created','modified')

admin.site.register(board, boardAdmin)
