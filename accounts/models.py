from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,)
    date_of_birth = models.DateField(blank=False, null=False)
    fav_movie = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)

    # @receiver(post_save, sender=CustomUser)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #     instance.profile.save()
    
    # @receiver(post_save, sender=CustomUser)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

#     def __str__(self):
#         return str(self.user)