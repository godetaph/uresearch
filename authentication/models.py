from django.db import models
from django.contrib.auth.models import(AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, username, email, last_name, first_name, middle_name, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        if last_name is None:
            raise TypeError('Last name is required')
        if first_name is None:
            raise TypeError('First name is required')
        if middle_name is None:
            raise TypeError('Middle name is required')

        user = self.model(username=username, email=self.normalize_email(email), last_name=last_name, first_name=first_name, middle_name=middle_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, last_name, first_name, middle_name, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email,last_name, first_name, middle_name,  password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
#                   'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    ACCOUNT_TYPE = [
        ('FACULTY', 'FACULTY'),
        ('STUDENT', 'STUDENT'),
        ('ADMIN', 'ADMIN'),
        ('STAFF', 'STAFF')
    ]

    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    ext_name = models.CharField(max_length=10, blank=True, null=True)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='media/user/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # auth_provider = models.CharField(
    #     max_length=255, blank=False,
    #     null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'first_name', 'middle_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }