from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from APDM.models import *
from APDM.serializers import *
from APDM.Repository.GenericRepository import GenericRepository
from rest_framework import permissions
from rest_framework import generics, mixins
import datetime
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CropProductionDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    queryset = GenericRepository(CropProduction).getAll()
    serializer_class = CropProductionSerializer

class CropProductionsByPlot(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    cropRepo = GenericRepository(CropProduction)

    def get(self, request, plot, format=None):
        crop_productions = self.cropRepo.filterBy("plot",plot,None)
        serializer = CropProductionSerializer(crop_productions, many= True)
        return Response(serializer.data)

class CropProductionByClient(generics.ListAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    cropClientRepo= GenericRepository(CropClient)
    cropRepo = GenericRepository(CropProduction)

    def get_crop_productions_by_client_ID(self, user):
        ids=self.cropClientRepo.filterBy("client_id",user.client_id,"crop_production_id")
        return self.cropRepo.filterBy("crop_production_id__in",ids,None)

    def get(self, request, format=None):
        crop_productions = self.get_crop_productions_by_client_ID(user=request.user)
        serializer = CropProductionSerializer(crop_productions, many= True)
        return Response(serializer.data)

class DiseasesByCropProduction(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    cropRepo = GenericRepository(CropProduction)

    def get(self, request, pk, format=None):
        crop_production = self.cropRepo.getBy("pk",pk)
        if(crop_production):
            serializer = DiseaseSerializer(crop_production.diseases, many= True)
            return Response(serializer.data)
        else:
            return HttpResponse("Crop not found")

class DiseaseDetail(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    diseaseRepo = GenericRepository(Disease)
    queryset = diseaseRepo.getAll()

    serializer_class = DiseaseSerializer
