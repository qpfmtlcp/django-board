from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class Board(TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')

    title = models.CharField(max_length=50)
    contents = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    



class History(TimeStampedModel):
    board = models.ForeignKey(
        Board,
        related_name='history',
        on_delete=models.CASCADE,
        null=False,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)