from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

# Create your models here.
'''
관리자만 생성/수정/삭제 가능 - serializer 에서 detail부분으로 들어가고 여기서 auth를 해야함 
아무나 조회는 가능 - 다만 get은 권한 없이 전부 가능하도록. 
게시글과 비슷한 수준의 모델로 구현 - board를 fk로 받아온다??
관리자는 장고 user의 is_manager 로 구분 - 권한 부분을 한번 재대로 해봐야될듯
'''


class NoticeBoard(TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')

    title = models.CharField(max_length=50)
    contents = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE
    )