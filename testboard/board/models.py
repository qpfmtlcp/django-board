from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

class User(models.Model):
    username = models.CharField(max_length = 30)

class Board (TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')
    title = models.CharField(max_length = 50)
    contents = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
