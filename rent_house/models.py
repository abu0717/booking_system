from django.db import models
from users.models import UserModel
from region.models import Country


# Create your models here.
class RentHouse(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    neighborhood = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    policy = models.CharField(max_length=100)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
