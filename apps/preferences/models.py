from django.db import models

from authentication.models import User


class Unit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['short_name',]

    def __str__(self):
        return self.short_name

class Unit1(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, related_name='unit1_unit', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['short_name',]

    def __str__(self):
        return self.short_name

class Unit2(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit1, related_name='unit1_unit', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['short_name',]

    def __str__(self):
        return self.short_name


class SemSy(models.Model):
    sem = models.CharField(max_length=20)
    sy = models.IntegerField()
    is_active = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='semsy_users', on_delete=models.CASCADE)