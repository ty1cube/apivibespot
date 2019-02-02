from django.conf.urls import url, include
from . import views, const_views
from rest_framework import routers
from .views import (
    LoginAPIView, 
    RegistrationAPIView, 
    LogoutAPIView,
    PasswordResetAPIView,
    PasswordResetVerifyAPIView,
    PasswordResetVerifiedAPIView,
    PasswordChangeAPIView,

)

router = routers.DefaultRouter()
# router.register('user', views.UserView)
# router.register('profile', views.ProfileView)
    

urlpatterns = [
    # url(r'^login/?$', views.CustomAuthToken.as_view()),
    url('login/?$', views.CustomAuthToken.as_view()),
    # url('login/?$', LoginAPIView.as_view()),
    url('register/?$', RegistrationAPIView.as_view()),
    # url('^user/?$', UserRetrieveUpdateAPIView.as_view()),
    # url('member/user/?$', views.UserDefaultMemberView.as_view()),
    # url('artist/?$', views.GetUserArtistMemberView.as_view()),
    # url('manager/?$', views.GetUserRecordMemberView.as_view()),
    # url('member/create/artist/?$', views.CreateArtistMemberView.as_view()),
    # url('member/create/manager/?$', views.CreateRecordMemberView.as_view()),
    url('logout/?$', LogoutAPIView.as_view(), name='authemail-logout'),
    url('password/reset/?$', PasswordResetAPIView.as_view(), name='password-reset'),
    url('^password/reset/verify/?$', PasswordResetVerifyAPIView.as_view(), name='password-reset-verify'),
    url('^password/reset/verified/?$', PasswordResetVerifiedAPIView.as_view(), name='password-reset-verified'),
    url('^password/change/?$', PasswordChangeAPIView.as_view(), name='password-change'),

    url('', include(router.urls)),

    url('country/?$', const_views.CountryView.as_view()),
    url('state/?$', const_views.StateView.as_view()),
    url('localarea/?$', const_views.LocalAreaView.as_view()),
    
]