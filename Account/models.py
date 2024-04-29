from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp=models.ImageField(upload_to='Account/media/dp_image/',null=True,blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return str(self.user.first_name)

class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length= 50)
    street_address = models.CharField(max_length=50)
    street_number=models.CharField(max_length=20)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)
    def __str__(self):
        return str(self.user.email)