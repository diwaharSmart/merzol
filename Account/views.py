from ipaddress import ip_address
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import random
# from account.models import DeviceVerification,User
from rest_framework.authtoken.models import Token
from django.core.files.images import ImageFile
from Account.models import User





class UserView(APIView):

    def get(self,request,format=None):
        mobile_number  = self.request.query_params.get('mobile_numner',None)
        try:
            user = User.objects.get(username=mobile_number),
            token , created = Token.objects.get_or_create(user=user)
            resp = dict()
            resp["name"] = user.first_name
            resp["profile_image"] = user.profile
            resp["user_id"] = user.user_id
            resp["status"] = user.status
            resp["country_code"] = user.country_code
            resp["token"] = token.key
            return Response(resp,status=status.HTTP_200_OK)
        except:
            return Response({},status=status.HTTP_204_NO_CONTENT)



    def post(self,request,format=None):
        import random
        data = request.data
        user = User(first_name=data["name"],username=data["username"],country_code=data["country_code"],status=data["status"])
        user.set_password(str(random.randint(100000000,9999999999999)))
        user.save()
        token , created = Token.objects.get_or_create(user=user)
        resp = dict()
        resp["name"] = user.first_name
        resp["profile_image"] = user.profile
        resp["user_id"] = user.user_id
        resp["status"] = user.status
        resp["country_code"] = user.country_code
        resp["token"] = token.key


        return Response(resp,status=status.HTTP_200_OK)



