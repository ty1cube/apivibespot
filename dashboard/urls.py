from django.conf.urls import url, include
from django.urls import include, path
# from . import views, const_views
from rest_framework import routers

from .views import (
    SongCreateAPIView,
    AlbumCreateAPIView,
    SongListAPIView,
    SongUpdateAPIView,
    SongDetailAPIView,
    AlbumListAPIView, 
    AlbumDetailAPIView,
    

)

router = routers.DefaultRouter()
# router.register('user', views.UserView)
# router.register('profile', views.ProfileView)


urlpatterns = [

    path('song/', SongListAPIView.as_view(), name='song'),
    path('song/add/', SongCreateAPIView.as_view(), name='addsong'),
    path('song/<int:pk>/', SongDetailAPIView.as_view(), name='detailsong'),
    path('song/<int:pk>/update/', SongUpdateAPIView.as_view(), name='updatesong'),
    path('album/', AlbumListAPIView.as_view(), name='album'),
    path('album/add/', AlbumCreateAPIView.as_view(), name='albumadd'),
    path('album/<int:pk>/', AlbumDetailAPIView.as_view(), name='albumlist')
    # path('password/reset/', PasswordResetAPIView.as_view(), name='password-reset'),


]
