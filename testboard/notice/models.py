from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

# Create your models here.


class NoticeBoard(TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')

    title = models.CharField(max_length=50)
    contents = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE
    )