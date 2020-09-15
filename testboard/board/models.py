from django.db import models

class board (models.Model):
    title = models.CharField(max_length = 50)
    contents = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField() 

    class Meta:
        ordering = ['created']
    