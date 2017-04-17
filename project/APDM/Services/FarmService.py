from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from APDM.models import *
from APDM.serializers import *
from rest_framework import permissions
from rest_framework import generics, mixins
import datetime
from oauth2_provider.models import AccessToken, Application
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from APDM.mongodb import *
import math
import xmlrpclib

class FarmList(generics.ListCreateAPIView):
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
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
