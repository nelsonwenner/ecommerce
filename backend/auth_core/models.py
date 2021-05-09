from django.contrib.auth.models import AbstractUser
from auth_core.managers import UserManager
from django.utils import timezone
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True, error_messages={
        'unique': ("A user with that email already exists."),
    })

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user auth'
