from django.db import models
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, send_mail
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, HttpResponse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(max_length=None, upload_to='images/', null=True, blank=True)
    imgPath = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject