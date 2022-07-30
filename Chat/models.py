from pyexpat import model
from django.db import models
from django.conf import settings
from Account.models import User
from Room.models import Room
# Create your models here.


ATTACHMENT_TYPE = (
    ('text','text'),
    ('image','image'),
    ('audio','audio'),
    ('document','document'),
    ('video','video'),
    ('voice_note','voice_note'),
    ('sticker','sticker'),
)

class Message(models.Model):
    room            = models.ForeignKey(Room,on_delete=models.CASCADE,blank=True,null=True)
    from_user       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name="from_user")
    to_user         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name="to_user")
    text            = models.TextField(max_length=3000,blank=True,null=True)
    reply           = models.CharField(max_length=255,blank=True,null=True)
    attachment_type = models.CharField(max_length=255,choices=ATTACHMENT_TYPE,default="text")
    media_attached  = models.URLField(blank=True,null=True)
    text            = models.BooleanField(default=False)
    media           = models.BooleanField(default=False)
    timestamp       = models.CharField(max_length=255,blank=True,null=True)
       


class MediaFile(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    file            = models.FileField(upload_to="message/file/")
    def __str__(self):
        return self.id