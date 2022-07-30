from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import random
# from account.models import DeviceVerification,User
from rest_framework.authtoken.models import Token
from Account.models import User
from Account.serializer import ContactSerializer
from Meeting.models import MEETING, PARTICIPANT
from Meeting.serializer import MeetingSerializer
# Create your views here.


class MeetingtView(APIView):

    def get(self,request,format=None):
        meetings = []
        res = []
        participant = PARTICIPANT.objects.filter(user=request.user,recieved=False)
        for i in participant:
            print(i.meeting)
            meetings.append(i.meeting)

        for i in meetings:
            serializer_data = {}
            contacts = []
            m = MEETING.objects.get(id=i.id)
            meeting         = MeetingSerializer(m).data
            for j in m.participants.all():
                contacts.append(ContactSerializer(j.user).data)

            serializer_data["meeting"]=meeting
            serializer_data["participants"]=contacts
            res.append(serializer_data)

        return Response(res,status=status.HTTP_200_OK)


    
    def post(self,request,format=None):      
        data = request.data
        serializer_data ={}
        contacts = []
        meeting = MEETING.objects.create(
            title=data["title"],
            status = data["status"],
        )

        for i in data["participants"]:
            participant = PARTICIPANT.objects.create(
                meeting =meeting,
                user = User.objects.get(user_id=i["user_id"]),
                admin = i["admin"],
                recieved = i["recieved"],
            )
            contacts.append(ContactSerializer( User.objects.get(user_id=i["user_id"])).data)

        

            
        meeting_serializer = MeetingSerializer(meeting)

        serializer_data["meeting"]=meeting_serializer.data
        serializer_data["participants"]=contacts


        return Response(serializer_data,status=status.HTTP_200_OK)