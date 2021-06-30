from django.db import models
from django.core.mail import BadHeaderError, send_mail
from django.db.models.deletion import CASCADE
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, send_mail
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User


# Create your models here.
class Like(models.Model):
    title = models.ForeignKey('Article', on_delete=CASCADE, null=True, blank=True)
    count = models.CharField(max_length=100, null=True, blank=True)
    who_liked = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(max_length=None, upload_to='images/', null=True, blank=True)
    imgPath = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(
        User,
        through='Like',
        through_fields=('title', 'who_liked')
    )
    published = models.DateTimeField(auto_now=False, auto_now_add=True)
    # models.PositiveIntegerField(null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-published']


    def __str__(self):
        return self.title


class ContactForm(models.Model):
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject