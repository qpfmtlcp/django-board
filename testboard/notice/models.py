from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class Tag(models.Model):
    tagname = models.CharField(max_length=100)

    def __str__(self):
        return self.tagname


class NoticeBoard(TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')

    title = models.CharField(max_length=50)
    contents = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag, through="TagListRelatedBoard")

    def __str__(self):
        return self.title


class TagListRelatedBoard(TimeStampedModel):
    notice = models.ForeignKey(NoticeBoard, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['notice', 'tag']]