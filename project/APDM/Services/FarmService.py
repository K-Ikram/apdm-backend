from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from APDM.models import *
from APDM.serializers import *
from rest_framework import permissions
from rest_framework import generics, mixins
import datetime
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class FarmList(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_farms(self, user):
        try:
            return Farm.objects.filter(clients=user)
        except Farm.DoesNotExist:
            raise Farm.DoesNotExist

    def get(self, request, format=None):
        farms= self.get_farms(user=request.user) # get the farms owned by this user
        serializer = FarmSerializer(farms, many=True)
        return Response(serializer.data)

class FarmDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
