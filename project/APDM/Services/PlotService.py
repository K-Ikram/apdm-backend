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

class PlotList(generics.ListCreateAPIView):

    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

class PlotsByFarm(APIView):

    def get_plots_by_farm_ID(self, farm):
        try:
            return list(Plot.objects.filter(farm=farm))
        except Plot.DoesNotExist:
            raise Http404

    def get(self, request, farm, format=None):
        plots = self.get_plots_by_farm_ID(farm)
        serializer = PlotSerializer(plots, many= True)
        return Response(serializer.data)

class PlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
