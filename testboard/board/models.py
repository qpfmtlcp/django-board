from django.db import models
from model_utils.models import TimeStampedModel

class board (TimeStampedModel):
    title = models.CharField(max_length = 50)
    contents = models.TextField()
