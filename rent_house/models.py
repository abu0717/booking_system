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


class ImagesContainer(models.Model):
    house = models.ForeignKey(RentHouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.house


class ImageModel(models.Model):
    image = models.ImageField(upload_to='rent_house/images/')
    image_collection = models.ForeignKey(ImagesContainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_collection.house