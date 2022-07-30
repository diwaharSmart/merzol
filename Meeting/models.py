
from django.db import models
import uuid
from django.conf import settings
# Create your models here.

STATUS = (
    ("live","live"),
    ("end","end"),
    ("upcoming","upcoming"),
)
class MEETING(models.Model):
    meeting_id = models.CharField(default=uuid.uuid4,unique=True,max_length=255)
    title      = models.CharField(max_length=255,blank=True,null=True)
    status     = models.CharField(default=STATUS,max_length=255,blank=True,null=True)
    created_at    = models.DateTimeField(auto_now_add = True,editable=False,blank=True,null=True)


class PARTICIPANT(models.Model):
    meeting      = models.ForeignKey(MEETING,blank=True,null=True,related_name="participants",on_delete=models.CASCADE)
    user         = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    recieved     = models.BooleanField(default=False)
    admin        = models.BooleanField(default=False)