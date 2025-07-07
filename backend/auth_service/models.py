from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=50, default='learner')  # e.g. learner, coach, admin
    tenant_id = models.CharField(max_length=100, blank=True)  # for multi-tenancy

    def __str__(self):
        return self.username
