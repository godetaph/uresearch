from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .serializers import PaperSerializer, AttachmentSerializer, PaperCommentSerializer, AttachmentCommentSerializer

from .models import Paper, Attachment, PaperComment, AttachmentComment

class PaperViewSet(viewsets.ModelViewSet):
    serializer_class = PaperSerializer
    queryset = Paper.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class AttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentSerializer
    queryset = Attachment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class PaperCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PaperCommentSerializer
    queryset = PaperComment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class AttachmentCommentViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentCommentSerializer
    queryset = AttachmentComment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)