from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

# Create your models here.


class Tag(models.Model):
    tagname = models.CharField(max_length=100)  # unique=True)
    # unique는 해당 필드가 테이블에서 유니크하게 저장됨. 중복되는 값이 있으면 오류 발생

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


# 태그를 링크처리. Charfiled로 받고 링크를 클릭하면 해당 링크가 포함된 post list 검색결과 나와야 함.
# custom template filter를 사용하고 many to many 를 활용해얗됨.
# notice와 tag모델은 many to many
