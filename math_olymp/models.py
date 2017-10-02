from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
'''
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    register_date = models.DateField(auto_now_add=True)
    paid_expire_date = models.DateField(auto_now=True)
    api_key = models.CharField(max_length=32, blank=True)

    @receiver(post_save, sender=User)
    def create_user_owner(sender, instance, created, **kwargs):
        if created:
            Owner.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_owner(sender, instance, **kwargs):
        instance.owner.save()

    def __str__(self):
        return self.user.username
'''