from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    # is_google_auth = models.BooleanField(default=False)
    # google_id      = models.TextField(max_length=1500,blank=True,null=True)

    status         = models.TextField(max_length=1500,blank=True,null=True)
    mobile_number  = models.CharField(max_length=255,blank=True,null=True,unique=True)
    user_id        = models.CharField(default=uuid.uuid4,max_length=255,unique=True)
    country_code   = models.CharField(max_length=255,blank=True,null=True)
    profile        = models.ImageField(upload_to = "user/profile/images/",blank=True,null=True)
    online         = models.BooleanField(default=False)
    last_seen      = models.CharField(max_length=255,blank=True,null=True)

