from rest_framework import serializers
from Meeting.models import *

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model= MEETING
        fields="__all__"

