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
from APDM.learningDataAccess import *

class RiskRates(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, crop, disease, format=None):
        learningDataAccess = LearningDataAccess()
        disease = Disease.objects.get(pk=disease)
        predictions = learningDataAccess.getRiskRates(int(crop), disease.disease_name)
        serializer = RiskRateSerializer(predictions, many= True)
        return Response(serializer.data)

class RiskRateByCrop(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, crop, format=None):
        learningDataAccess = LearningDataAccess()
        crop_production = CropProduction.objects.get(pk=crop)
        # recuperer la liste des maladies surveillees pour cette culture
        serializer = DiseaseSerializer(crop_production.diseases, many = True)
        predictions =[]

        for disease in serializer.data:
            # recuperer les dn predictions les plus recentes de cette culture
            pred = learningDataAccess.getLastRiskRate(int(crop),disease["disease_name"])
            if (pred is not None):
                predictions.append(pred)
                print pred
        # retourner la liste des predictions
        serializer = RiskRateSerializer(predictions, many= True)
        return Response(serializer.data)
