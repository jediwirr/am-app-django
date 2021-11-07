from django.urls import path, include
from .views import Categories, ArticleDetails, Articles, UserViewset, LikeViewset, CommentViewset, article_details, like_details, send_email, article_list, user_details, comment_details
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

#article_list, article_details

router = DefaultRouter()
# router.register('articles', ArticleViewSet, basename="articles")
router.register('users', UserViewset)
router.register('likes', LikeViewset)
router.register('comments', CommentViewset)
#router.register('emails', ContactFormViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tokens/', views.obtain_auth_token),
    path('api/emails/', send_email),
    path('api/articles/', article_list),
    path('api/articles/<int:pk>/', article_details),
    path('api/users/profile/<str:username>/', user_details),
    path('api/likes/like/<str:count>/', like_details),
    path('api/comments/comment/<str:count>/', comment_details),
    path('categories/', Categories.as_view(), name='categories'),
    path('articles/', Articles.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetails.as_view(), name='article'),
]
