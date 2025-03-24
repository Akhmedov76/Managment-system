from django.contrib.auth.models import AbstractUser
from django.db import models
from departments.models import Department


class CustomUser(AbstractUser):
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
