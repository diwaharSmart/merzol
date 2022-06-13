from attr import fields
from rest_framework import serializers
from Account.models import User

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['user_id','first_name','username','profile']