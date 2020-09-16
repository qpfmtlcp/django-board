from django.contrib import admin
from .models import Board, User

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'contents', 'created','modified')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(Board, BoardAdmin)
admin.site.register(User, UserAdmin)
