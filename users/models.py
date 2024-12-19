from django.db import models
from django.contrib.auth.models import User
from localflavor.pk.models import PKStateField, PKPostCodeField
from .utils import get_user_directory
# Create your models here.

class Location(models.Model):
    address_1 = models.CharField(max_length=250, null = False)
    address_2 = models.CharField(max_length=250, null = False)
    city = models.CharField(max_length=100)
    state = PKStateField(default = 'Punjab', null= False)
    post_code = PKPostCodeField(default='1111', null=False)


class Profile (models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to= get_user_directory, null = True)
    bio = models.TextField(max_length = 140)
    phone_number = models.CharField(max_length = 11, blank = False)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username}\' Profile'
    
    
