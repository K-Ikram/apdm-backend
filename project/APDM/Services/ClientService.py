from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from APDM.models import *
from APDM.serializers import *
from APDM.Repository.GenericRepository import GenericRepository
from rest_framework import permissions
from rest_framework import generics, mixins
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated

class CurrentClient(APIView):
     authentication_classes = [OAuth2Authentication]
     permission_classes = [IsAuthenticated]
     clientRepo = GenericRepository(Client)

     def get(self, request, format=None):
        client= self.clientRepo.getBy("pk",request.user.client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

class ClientByUsername(APIView):
     clientRepo = GenericRepository(Client)
     def get(self, request,username, format=None):
         client= self.clientRepo.getBy("username",username)
         if(client is not None):
             serializer = ClientSerializer(client)
             return Response(serializer.data)
         else:
             return HttpResponse("Client doesn't exist")

class UpdateProfile(generics.RetrieveUpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    clientRepo = GenericRepository(Client)
    queryset = clientRepo.getAll()
    serializer_class = ClientSerializer

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    model = Client

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
