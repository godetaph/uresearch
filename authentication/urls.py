from os import name
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenRefreshView,)

from.views import LogoutAPIView, RegisterView, UserDetailAPIView, UserListAPIView, VerifyEmail, LoginAPIView, RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView

# router = DefaultRouter()
# router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='users'),
    path('users/<int:id>', UserDetailAPIView.as_view(), name='user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]
