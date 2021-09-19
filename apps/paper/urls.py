from rest_framework import urlpatterns 
from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import PaperViewSet, AttachmentViewSet, PaperCommentViewSet, AttachmentCommentViewSet

router = DefaultRouter()
router.register('papers', PaperViewSet, basename='papers')
router.register('attachments', AttachmentViewSet, basename='attachments')
router.register('paper-comments', PaperCommentViewSet, basename='paper-comments')
router.register('attachment-comments', AttachmentCommentViewSet, basename='attachment-comments')

urlpatterns = [
    path('', include(router.urls)),
]
