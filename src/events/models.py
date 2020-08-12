from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager, SearchManager
from jsonfield import JSONField
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    events = JSONField()
    interests = JSONField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    age = models.IntegerField(default=0)
    institution = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

class HappeningEvents(models.Model):
    name = models.CharField(max_length=100, unique=True)
    poster = models.ImageField(upload_to='media/')
    organizer = models.ForeignKey(User, related_name='myevents', on_delete=models.CASCADE)
    participants = JSONField()
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=4096)
    event_type = JSONField()
    contact_number = models.CharField(max_length=15)
    event_date = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name