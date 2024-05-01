from django.db import models
from django.contrib.auth.models import User
from .validation import validate_password


# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    password = models.CharField(max_length=100, validators=[validate_password])
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
