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

class CropProductionList(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    queryset = CropProduction.objects.all()
    serializer_class = CropProductionSerializer

class CropProductionDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    queryset = CropProduction.objects.all()
    serializer_class = CropProductionSerializer

class CropProductionsByPlot(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_crop_productions_by_client_ID(self, user):
        try:
            crops=list(CropClient.objects.filter(client_id=user.client_id))
            liste=[]
            for crop in crops:
                 liste.append(crop.crop_production_id)
            return list(CropProduction.objects.filter(crop_production_id__in =liste))
        except CropClient.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        crop_productions = self.get_crop_productions_by_client_ID(user=request.user)
        print("==> crops",crop_productions)
        serializer = CropProductionSerializer(crop_productions, many= True)
        return Response(serializer.data)

class DiseasesByCropProduction(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
