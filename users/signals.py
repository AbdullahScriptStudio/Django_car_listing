from django.db.models.signals import post_save
from django.contrib.auth.models import User
from  .models import Profile, Location
from django.dispatch import receiver



@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        

@receiver(post_save, sender= Profile)
def create_location_profile(sender, instance, created,  **kwargs):
    if created:
        loc = Location.objects.create()
        instance.location = loc
        instance.save()
        