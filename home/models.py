import uuid
from django.db import models
from home.consts import CAR_BRANDS, TRANSMISSION_OPTIONS
from home.utils import get_listings_directory
from users.models import Profile, Location
from localflavor.us.models import USStateField
# Create your models here.


class Listings(models.Model):
    id = models.UUIDField(
        primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    dealer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    brand = models.CharField(choices=CAR_BRANDS, max_length=60, default= 'BMW')
    model = models.CharField(max_length=4)
    vin = models.CharField(max_length=130)
    color = models.CharField(max_length=50, default= 'white')
    description = models.TextField()
    milage = models.CharField(max_length=50)
    #location = models.CharField(max_length=255, null=True, blank=True)
    transmission = models.CharField(max_length=50, choices= TRANSMISSION_OPTIONS)
    pic = models.ImageField( upload_to=get_listings_directory)
    


class Listing101(models.Model):
    id = models.UUIDField(
        primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    dealer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    brand = models.CharField(choices=CAR_BRANDS, max_length=60, default= 'BMW')
    model = models.CharField(max_length=4)
    vin = models.CharField(max_length=130)
    color = models.CharField(max_length=50, default= 'white')
    description = models.TextField()
    milage = models.CharField(max_length=50)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    transmission = models.CharField(max_length=50, choices= TRANSMISSION_OPTIONS)
    pic = models.ImageField( upload_to=get_listings_directory)
    
    def __str__(self):
        return f'{self.dealer.user.username}\Listings {self.model}'