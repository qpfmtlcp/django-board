from django.db import models
from model_utils import Choices

# Create your models here.
class Questionboard(models.Model):
    STATUS      = Choices('question', 'answser')
    title       = models.CharField(max_length=50)
    content     = models.TextField()

class AnswerBoard(models.Model):
    question    = models.ForeignKey(Questionboard, on_delete=models.CASCADE)
    content     = models.TextField()
    score       = models.IntegerField()
     