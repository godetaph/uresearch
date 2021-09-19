from rest_framework import serializers

from .models import Unit, Unit1, Unit2, SemSy

class UnitSerializer(serializers.Serializer):
    class Meta:
        model = Unit
        fields = ['id', 'name', 'short_name', 'created_on', 'modified_on',]

class Unit1Serializer(serializers.Serializer):
    class Meta:
        model = Unit1
        fields = ['id', 'name', 'short_name', 'unit', 'created_on', 'modified_on',]

class Unit2Serializer(serializers.Serializer):
    class Meta:
        model = Unit2
        fields = ['id', 'name', 'short_name', 'unit1', 'created_on', 'modified_on',]

class SemSySerializer(serializers.Serializer):
    class Meta:
        model = SemSy
        fields = ['id', 'sem', 'sy', 'is_active', 'created_on', 'modified_on', 'created_by',]