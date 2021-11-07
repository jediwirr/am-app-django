from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article, ContactForm, Like, Comment
from .serializers import ArticleSerializer, LikeSerializer, UserSerializer, ContactFormSerializer, CommentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .notifications import send_push_message
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.views import APIView
import requests

@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def article_list(request):
    uri = 'https://exp.host/--/api/v2/push/send'
    token = 'ExponentPushToken[9NU5RiH1dO7LyVWewfEfqk]'
    title = request.POST.get('title', '')
    body = request.POST.get('description', '')

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            requests.post(uri, data = {"to": token, "title": title, "body": body})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Categories(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cats.html'

    def get(self, request):
        queryset = Article.objects.all()
        return Response({'articles': queryset})


class Articles(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'articles.html'

    def get(self, request):
        queryset = Article.objects.all()
        return Response({'articles': queryset})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('articles')


class ArticleDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article.html'

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response({'serializer': serializer, 'article': article})


@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, username):
    try:
        user = User.objects.get(username=username)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeViewset(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


@api_view(['GET', 'DELETE'])
def like_details(request, count):
    try:
        like = Like.objects.get(count=count)

    except Like.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LikeSerializer(like)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET', 'DELETE'])
def comment_details(request, count):
    try:
        comment = Comment.objects.get(count=count)

    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
class ContactFormViewset(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def send_email(request):
        if request.method == 'POST':
            send_mail(
                'anohai',
                'igogo',
                'andm1793@gmail.com',
                ['andm1793@gmail.com'],
                fail_silently=False,
            )
'''

@api_view(['GET', 'POST'])
def send_email(request):
    
    if request.method == 'GET':
        forms = ContactForm.objects.all()
        serializer = ContactFormSerializer(forms, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        send_mail(
            subject,
            message,
            'andm1793@gmail.com',
            [email],
            fail_silently=False,
        )
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



'''
class ArticleList(generics.GenericAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class ArticleDetails(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)

'''


'''
class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
