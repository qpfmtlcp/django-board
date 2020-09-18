from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class User(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.username)


class Board(TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')

    title = models.CharField(max_length=50)
    contents = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class History(TimeStampedModel):
    board = models.ForeignKey(
        Board, related_name='history', on_delete=models.CASCADE, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
