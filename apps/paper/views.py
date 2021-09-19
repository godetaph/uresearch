from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .serializers import PaperSerializer

from .models import Paper

class PaperViewSet(viewsets.ModelViewSet):
    serializer_class = PaperSerializer
    queryset = Paper.objects.all()
    permission_classes = (permissions.IsAuthenticated,)