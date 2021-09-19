from rest_framework import urlpatterns 
from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import PaperViewSet

router = DefaultRouter()
router.register('papers', PaperViewSet, basename='papers')

urlpatterns = [
    path('', include(router.urls)),
]
