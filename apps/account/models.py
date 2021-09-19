from django.db import models

from authentication.models import User
from apps.preferences.models import Unit2

class Account(models.Model):
    user = models.ForeignKey(User, related_name='account_users', on_delete=models.CASCADE)
    course = models.ForeignKey(Unit2, related_name='account_unit2', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='account_created', on_delete=models.CASCADE)
    yr = models.IntegerField(default=4, blank=True, null=True)
    sec = models.CharField(max_length=20, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_now_add=True)