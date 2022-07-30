from rest_framework import serializers
from Meeting.models import *
from Account.serializer import ContactSerializer

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model= MEETING
        fields="__all__"

class ParticipantSerializer(serializers.ModelSerializer):
    user = ContactSerializer()
    class Meta:
        model= PARTICIPANT
        fields="__all__"