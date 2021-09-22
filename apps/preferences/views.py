from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import UnitSerializer, Unit1Serializer, Unit2Serializer, SemSySerializer
from .models import Unit, Unit1, Unit2, SemSy

# class UnitListAPIView(ListCreateAPIView):
#     serializer_class = UnitSerializer
#     queryset = Unit.objects.all()
#     permisstion_classes = [permissions.IsAuthenticated,]

# class UnitDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = UnitSerializer
#     queryset = Unit.objects.all()
#     permisstion_classes = [permissions.IsAuthenticated,]
#     lookup_field = 'id'


class Unit1ViewSet(viewsets.ModelViewSet):
    serializer_class = Unit1Serializer
    queryset = Unit1.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class Unit2ViewSet(viewsets.ModelViewSet):
    serializer_class = Unit2Serializer
    queryset = Unit2.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class SemSyViewSet(viewsets.ModelViewSet):
    serializer_class = SemSySerializer
    queryset = SemSy.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class Unit1ViewSet(viewsets.ModelViewSet):
    serializer_class = Unit1Serializer
    queryset = Unit1.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class Unit2ViewSet(viewsets.ModelViewSet):
    serializer_class = Unit2Serializer
    queryset = Unit2.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class SemSyViewSet(viewsets.ModelViewSet):
    serializer_class = SemSySerializer
    queryset = SemSy.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
