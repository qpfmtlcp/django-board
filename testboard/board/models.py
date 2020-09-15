from django.db import models
#from model_utils.fields import StatusField
#from model_utils import Choices

# Create your models here.

class board (models.Model):
    title = models.CharField(max_length = 50)
    #modify: contents charfield > textfield로 변경
    contents = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField() 
    #to-do: 선택형 model 완성
    #status = models.CharField(choices=STATUS_CHOICES, default = published)

    #to-do: Meta클래스 찾아보기
    class Meta:
        ordering = ['created']
    


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