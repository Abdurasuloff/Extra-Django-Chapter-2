from django.contrib import admin
from .models import Profile, ChatGroup, Message

# Register your models here.


admin.site.register([Profile, ChatGroup, Message])