from django.db import models
from model_utils.models import StatusModel, TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices

class board (TimeStampedModel):
    STATUS = Choices('draft', 'published')
    title = models.CharField(max_length = 50)
    contents = models.TextField() 

    class Meta:
        ordering = ['created']
    