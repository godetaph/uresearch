from rest_framework import serializers

from .models import Paper

class PaperSerializer(serializers.Serializer):
    class Meta:
        model = Paper
        fields = ['proponent1', 'proponent2', 'proponent3', 'mode', 'title', 'abstract', 'slug', 
                    'is_accepted', 'adviser', 'co_adviser', 'created_by', 'created_on', 'modified_on']
    