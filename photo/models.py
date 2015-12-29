#from __future__ import unicode_literals
# coding: utf-8

from django.db import models

# Create your models here.
class Photo(models.Model):
    #id = '개별 사진을 구분하는 색인값'
    image_file = models.ImageField()
    filtered_image_file = models.ImageField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
