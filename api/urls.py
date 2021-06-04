from django.urls import path, include
from .views import ArticleViewSet, UserViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

#article_list, article_details

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename="articles")
router.register('users', UserViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tokens/', views.obtain_auth_token)
   # url(r'api/', include('api.urls')),

    # url(r'^auth/login/$',
    #    obtain_auth_token,
    #    name='auth_user_login'),
    # url(r'^auth/register/$',
    #    CreateUserAPIView.as_view(),
    #    name='auth_user_create'),
    # url(r'^auth/logout/$',
    #    LogoutUserAPIView.as_view(),
    #    name='auth_user_logout')

    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:pk>/', ArticleDetails.as_view()),

    #path('articles/', article_list),
    #path('articles/<int:pk>/', article_details),

]
