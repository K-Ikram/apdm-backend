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

class CropProductionList(generics.ListCreateAPIView):

    queryset = CropProduction.objects.all()
    serializer_class = CropProductionSerializer

class CropProductionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = CropProduction.objects.all()
    serializer_class = CropProductionSerializer

class CropProductionsByPlot(APIView):

    def get_crop_productions_by_plot_ID(self, plot):
        try:
            return list(CropProduction.objects.filter(plot=plot))
        except CropProduction.DoesNotExist:
            raise Http404

    def get(self, request, plot, format=None):
        crop_productions = self.get_crop_productions_by_plot_ID(plot)
        serializer = CropProductionSerializer(crop_productions, many= True)
        return Response(serializer.data)

class CropProductionByClient(generics.ListAPIView):

    def get_crop_productions_by_client_ID(self, user):
        try:
            crops=list(CropClient.objects.filter(client=user))
            liste=[]
            for crop in crops:
                 liste.append(crop.crop_production.crop_production_id)
            return list(CropProduction.objects.filter(crop_production_id__in =liste))
        except CropClient.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        crop_productions = self.get_crop_productions_by_client_ID(user=request.user)
        print("==> crops",crop_productions)
        serializer = CropProductionSerializer(crop_productions, many= True)
        return Response(serializer.data)

class DiseasesByCropProduction(APIView):
    def get_object(self, pk):
        try:
            return CropProduction.objects.get(pk=pk)
        except CropProduction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        crop_production = self.get_object(pk)

        serializer = DiseaseSerializer(crop_production.diseases, many= True)
        return Response(serializer.data)

class DiseaseDetail(generics.RetrieveAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer