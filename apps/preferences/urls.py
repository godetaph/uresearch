from os import name
from rest_framework import urlpatterns 
from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import UnitViewSet, Unit1ViewSet, Unit2ViewSet, SemSyViewSet
# from .views import UnitListAPIView

router = DefaultRouter()
router.register('units', UnitViewSet, basename='units')
router.register('unit1s', Unit1ViewSet, basename='unit1s')
router.register('unit2s', Unit2ViewSet, basename='unit2s')
router.register('semsy', SemSyViewSet, basename='semsy')

urlpatterns = [
    path('', include(router.urls)),
    # path('units/', UnitListAPIView.as_view(), name='units' )
]
