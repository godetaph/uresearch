from rest_framework import serializers

from .models import Unit, Unit1, Unit2, SemSy

#this for colleges
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name', 'short_name', 'created_on', 'modified_on',]

#this is for department
class Unit1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Unit1
        fields = ['id', 'name', 'short_name', 'unit', 'created_on', 'modified_on',]

#this is for the courses
class Unit2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Unit2
        fields = ['id', 'name', 'short_name', 'unit', 'created_on', 'modified_on',]

#this is for the semester and schoolyear
class SemSySerializer(serializers.ModelSerializer):
    class Meta:
        model = SemSy
        fields = ['id', 'sem', 'sy', 'is_active', 'created_on', 'modified_on', 'created_by',]