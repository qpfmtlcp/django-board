from django.contrib import admin
from .models import board
# Register your models here.
# models.py 에 작성한 class 등록 

class boardAdmin(admin.ModelAdmin):
    list_display = ('title', 'contents', 'modified')

admin.site.register(board, boardAdmin)
