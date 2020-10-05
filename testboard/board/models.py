from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class Tag(models.Model):
    tagname = models.CharField(max_length=100)
    slug    = models.SlugField(unique =True)
    
    def __str__(self):
        return "#" + self.tagname
    
class Board(TimeStampedModel, StatusModel):
    STATUS  = Choices('draft', 'published')

    title   = models.CharField(max_length=50)
    contents= models.TextField()
    owner   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image   = models.ImageField(null=True, blank=True, upload_to='image/')
    tag     = models.ManyToManyField(Tag, related_name='board')


class History(TimeStampedModel):
    board   = models.ForeignKey(
        Board,
        related_name='history',
        on_delete   =models.CASCADE,
        null        =False,
    )
    user    = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    