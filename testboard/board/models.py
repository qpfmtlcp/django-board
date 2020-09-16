from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

class board (TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')
    title = models.CharField(max_length = 50)
    contents = models.TextField() 
    