from django.conf.urls import url, include
from django.urls import include, path
from . import views, const_views
from rest_framework import routers

from .views import (
    # LoginAPIView,
    RegistrationAPIView,
    RegisterArtistAPIView,
    RegisterRecordLabelAPIView,
    RegisterManagerAPIView,
    #     UserRetrieveUpdateAPIView,
    LogoutAPIView,
    PasswordResetAPIView,
    PasswordResetVerifyAPIView,
    PasswordResetVerifiedAPIView,
    PasswordChangeAPIView,
    #     StateDetailAPIView,
    #     LocalAreaDetailAPIView,
)

router = routers.DefaultRouter()

router.register('user', views.UserView)
# router.register('profile', views.ProfileView)

urlpatterns = [
    # url(r'^login/?$', views.CustomAuthToken.as_view()),
    path('login/', views.CustomAuthToken.as_view()),
    #path('login/', LoginAPIView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
    #     path('user/', UserRetrieveUpdateAPIView.as_view()),
    # url('member/user/?$', views.UserDefaultMemberView.as_view()),
    # url('artist/?$', views.GetUserArtistMemberView.as_view()),
    # url('manager/?$', views.GetUserRecordMemberView.as_view()),

    url('register/artist/?$', RegisterArtistAPIView.as_view()),
    url('register/record_label/?$', RegisterRecordLabelAPIView.as_view()),
    url('register/manager/?$', RegisterManagerAPIView.as_view()),

    path('logout/', LogoutAPIView.as_view(), name='authemail-logout'),
    path('password/reset/', PasswordResetAPIView.as_view(), name='password-reset'),
    path('password/reset/verify/', PasswordResetVerifyAPIView.as_view(),
         name='password-reset-verify'),
    path('password/reset/verified/',
         PasswordResetVerifiedAPIView.as_view(), name='password-reset-verified'),
    path('password/change/', PasswordChangeAPIView.as_view(),
         name='password-change'),

    path('', include(router.urls)),

    path('country/', const_views.CountryView.as_view()),
    path('state/', const_views.StateView.as_view()),
    path('state/<int:pk>/', const_views.StateDetailAPIView.as_view(),
         name='statedetail'),
    path('localarea/', const_views.LocalAreaView.as_view()),
    path('localarea/<int:pk>/',
         const_views.LocalAreaDetailAPIView.as_view(), name='localdetail'),

]
