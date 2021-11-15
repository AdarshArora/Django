from django.db import models
from django.db.models.base import Model

# Create your models here.
class FileUpload(models.Model):
    myfiles = models.FileField(upload_to="")

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

