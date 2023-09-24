from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class ChatGroup(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)
    

class Message(models.Model):
    chatgroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, default='offline')
    picture = models.ImageField(upload_to="user_images/")

    def __str__(self):
        return f"Profile of {str(self.user.username)}"
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)