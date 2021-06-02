from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(max_length=None, upload_to='images/', null=True, blank=True)
    imgPath = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
