from django.db import models


class Todo(models.Model):
    task = models.TextField()
    label = models.ManyToManyField('todo.Label', related_name='todos')


class Label(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
