from django.db import models

# Create your models here.
# models.py
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
