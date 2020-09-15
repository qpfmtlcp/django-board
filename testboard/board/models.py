from django.db import models
#from model_utils.fields import StatusField
#from model_utils import Choices

# Create your models here.

class board (models.Model):
    title = models.CharField(max_length = 50)
    contents = models.CharField(max_length = 200) 
    created = models.DateTimeField()
    modified = models.DateTimeField() 
#django에서도 timestamp를 지원하지만 model util을 쓰면 좀더 편하게 사용이 가능하다.
# 링크된 문서 참고
#class status (models.Model):


'''
model {
  title
  contents
  created
  modified
}
'''