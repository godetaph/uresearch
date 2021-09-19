from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Paper, Attachment, PaperComment, AttachmentComment

class PaperSerializer(serializers.Serializer):
    class Meta:
        model = Paper
        fields = ['id', 'proponent1', 'proponent2', 'proponent3', 'semsy', 'course', 'mode', 'title', 'abstract', 'slug', 
                    'is_accepted', 'adviser', 'co_adviser', 'created_by', 'created_on', 'modified_on',]

class AttachmentSerializer(serializers.Serializer):
    class Meta:
        model = Attachment
        fields = ['id', 'paper', 'attachment', 'attachment1', 'attach_title', 'description',
                    'created_by', 'created_on', 'modified_on',]

class PaperCommentSerializer(serializers.Serializer):
    class Meta:
        model = PaperComment
        fields = ['id', 'paper', 'paper_comment', 
                    'created_by', 'created_on', 'modified_on',]

class AttachmentCommentSerializer(serializers.Serializer):
    class Meata:
        model = AttachmentComment
        fields = ['id', 'attachment', 'attachment_coment',
                    'created_by', 'created_on', 'modified_on',]