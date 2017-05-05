from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from APDM.models import *
from APDM.serializers import *
from rest_framework import permissions
import datetime
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import jsonrpclib
from django.conf import settings
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins

class AddAnomaly(generics.ListCreateAPIView):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user, reporting_date=datetime.datetime.now().replace(microsecond=0) )
        # start update training set
        disease = Disease.objects.get(pk=serializer.data['disease'])
        server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
        server.penalize(serializer.data['occurence_date'],disease.disease_name,serializer.data['crop_production'])

        # end update training set
