from distutils.archive_util import make_zipfile
from operator import mod
from statistics import mode
from django.db import models
from django.forms import model_to_dict

# Create your models here.

class OfferedCourse(models.Model):
    id=models.CharField(max_length=50,primary_key=True,null=False,blank=False,verbose_name="Course ID")
    name=models.CharField(max_length=100,null=False,blank=False,verbose_name="Course Name")
    description=models.CharField(max_length=150,null=False,blank=True,verbose_name="Description")
