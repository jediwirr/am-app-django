from django.urls import path, include
from .views import LikeViewset, UserViewset, article_details, send_email, article_list
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

#article_list, article_details

router = DefaultRouter()
# router.register('articles', ArticleViewSet, basename="articles")
router.register('users', UserViewset)
router.register('likes', LikeViewset)
#router.register('emails', ContactFormViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tokens/', views.obtain_auth_token),
    path('api/emails/', send_email),
    path('api/articles/', article_list),
    path('api/articles/<int:pk>/', article_details)

#    url(r'api/', include('api.urls')),

    # url(r'^auth/login/$',
    #    obtain_auth_token,
    #    name='auth_user_login'),
    # url(r'^auth/register/$',
    #    CreateUserAPIView.as_view(),
    #    name='auth_user_create'),
    # url(r'^auth/logout/$',
    #    LogoutUserAPIView.as_view(),
    #    name='auth_user_logout')

    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:pk>/', ArticleDetails.as_view()),

    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),

]
