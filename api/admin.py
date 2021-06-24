from django.contrib import admin
from .models import Article, ContactForm, Like

# Register your models here.

#admin.site.register(Article)

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')

@admin.register(Like)
class LikeModel(admin.ModelAdmin):
    list_filter = ('title', 'who_liked')
    list_display = ('title', 'count')

@admin.register(ContactForm)
class ContactFormModel(admin.ModelAdmin):
    list_filter = ('email', 'subject')
    list_display = ('email', 'subject')

