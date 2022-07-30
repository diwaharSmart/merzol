from distutils.command.upload import upload
from django.db import models
from django.conf import settings
# Create your models here.


class Room(models.Model):
    title         = models.CharField(max_length=255,blank=True,null=True)
    image         = models.ImageField(upload_to="room/image",blank=True,null=True)
    description   = models.CharField(max_length=255,blank=True,null=True)
    active        = models.BooleanField(default=False)
    group         = models.BooleanField(default=False)
    meeting       = models.BooleanField(default=False)
    private       = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.id


class RoomUser(models.Model):
    room         = models.ForeignKey(Room,on_delete=models.CASCADE,blank=True,null=True,related_name="room_user")
    participant  = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    last_visit   = models.CharField(max_length=255,blank=True,null=True)
    admin        = models.BooleanField(default=False)

    

