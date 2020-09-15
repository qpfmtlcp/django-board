from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.

class board (models.Model):
    title = models.CharField(max_length = 50)
    contents = models.CharField(max_length = 200) 
    created = models.DateTimeField('date_created')
    modified = models.DateTimeField('date_modified') 

#class status (models.Model):

#createsuperuser

'''
model {
  title
  contents
  created
  modified
}
'''