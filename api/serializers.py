from rest_framework import serializers
from .models import Article, ContactForm, Like, Comment
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from django.core.mail import send_mail


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'web_uri', 'category', 'title', 'image', 'imgPath', 'description', 'content', 'likes', 'published', 'comments']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['title', 'count', 'who_liked']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article_id', 'count', 'by_user', 'message', 'published']        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

        users = serializers.HyperlinkedRelatedField(
            view_name='user-detail',
            lookup_field='username',
            many=True,
            read_only=True
        )

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['email', 'subject', 'message']
