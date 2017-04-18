from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from APDM.models import *
from APDM.serializers import *
from rest_framework import permissions
from rest_framework import generics, mixins
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from APDM.mongodb import *
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
class CurrentClient(APIView):
     authentication_classes = [OAuth2Authentication]
     permission_classes = [IsAuthenticated]
     def get_client(self, user):
        try:
            return Client.objects.get(client_id=user)
        except Client.DoesNotExist:
            raise Client.DoesNotExist

     def get(self, request, format=None):
        client= self.get_client(user=request.user.client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

class ClientByUsername(APIView):
     def get_client(self, username):
        try:
            return Client.objects.get(username=username)
        except Client.DoesNotExist:
            raise Client.DoesNotExist

     def get(self, request,username, format=None):
        try:
            client= self.get_client(username=username)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except Client.DoesNotExist:
            return HttpResponse("Client doesn't exist")

class UpdateProfile(generics.RetrieveUpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
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
