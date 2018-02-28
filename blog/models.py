from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_lengh=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
