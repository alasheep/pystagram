#from __future__ import unicode_literals
# coding: utf-8

from django.db import models

# Create your models here.
class Photo(models.Model):
    #id = '개별 사진을 구분하는 색인값'
    image_file = models.ImageField(upload_to='%Y/%m/%d')
    filtered_image_file = models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d')
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image_file.delete()
        super(Photo, self).delete(*args, **kwargs)
