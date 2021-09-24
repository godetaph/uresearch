from apps.preferences.models import SemSy
from django.db import models
from django.db.models.base import Model

from authentication.models import User
from apps.account.models import Account
from apps.preferences.models import SemSy, Unit2, ReserchLevel

class Paper(models.Model):
    CAPSTONE = 'CAPSTONE'
    THESIS = 'THESIS'
    RESEARCH_TYPE =[
        (CAPSTONE,'CAPSTONE'),
        (THESIS, 'THESIS')
    ]

    proponent1 = models.ForeignKey(User, related_name='paper_proponent1', on_delete=models.CASCADE)
    proponent2 = models.ForeignKey(User, related_name='paper_proponent2', on_delete=models.CASCADE, blank=True, null=True)
    proponent3 = models.ForeignKey(User, related_name='paper_proponent3', on_delete=models.CASCADE, blank=True, null=True)
    semsy = models.ForeignKey(SemSy, related_name='paper_semsy', on_delete=models.CASCADE)
    course = models.ForeignKey(Unit2, related_name='paper_course', on_delete=models.CASCADE, blank=True, null=True)
    mode = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    research_level = models.ForeignKey(ReserchLevel, related_name='paper_research_level', on_delete=models.CASCADE)
    research_type = models.CharField(max_length=50, choices=RESEARCH_TYPE, default=THESIS)
    note = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    is_accepted = models.BooleanField(default=False)
    adviser = models.ForeignKey(User, related_name='paper_adviser', on_delete=models.CASCADE)
    co_adviser = models.ForeignKey(User, related_name='paper_co_adviser', on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='paper_created', on_delete=models.CASCADE, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

class Attachment(models.Model):
    paper = models.ForeignKey(Paper, related_name='attachment_papers', on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='file/attachment/', blank=True, null=True)
    attachment1 = models.TextField(blank=True, null=True)
    attach_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='attachment_papers', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

class PaperComment(models.Model):
    paper = models.ForeignKey(Paper, related_name='paper_comment_papers', on_delete=models.CASCADE)
    paper_comment = models.TextField()
    created_by = models.ForeignKey(User, related_name='paper_comment_created', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

class AttachmentComment(models.Model):
    attachment = models.ForeignKey(Attachment, related_name='attachement_comment_attachments', on_delete=models.CASCADE)
    attachment_comment = models.TextField()
    created_by = models.ForeignKey(User, related_name='attachment_comment_created', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)