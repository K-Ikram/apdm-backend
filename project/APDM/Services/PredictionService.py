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
from APDM.learningDataAccess import *

class RiskRates(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    diseaseRepo = GenericRepository(Disease)

    def get(self, request, crop, disease, format=None):
        learningDataAccess = LearningDataAccess()
        disease = self.diseaseRepo.getBy("pk",disease)
        if(disease):
            predictions = learningDataAccess.getRiskRates(int(crop), disease.disease_name)
            serializer = RiskRateSerializer(predictions, many= True)
            return Response(serializer.data)
        else:
            return HttpResponse("No disease found with that ID")

class RiskRateByCrop(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    cropRepo = GenericRepository(CropProduction)

    def get(self, request, crop, format=None):
        learningDataAccess = LearningDataAccess()
        crop_production = self.cropRepo.getBy("pk",crop)
        # recuperer la liste des maladies surveillees pour cette culture
        if(crop_production is None):
            return HttpResponse("No crop found with that ID")
        serializer = DiseaseSerializer(crop_production.diseases, many = True)
        predictions =[]

        for disease in serializer.data:
            # recuperer les dn predictions les plus recentes de cette culture
            pred = learningDataAccess.getLastRiskRate(int(crop),disease["disease_name"])
            if (pred):
                predictions.append(pred)
                print pred
        # retourner la liste des predictions
        serializer = RiskRateSerializer(predictions, many= True)
        return Response(serializer.data)
import jsonrpclib
class CurrentRiskRates(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    cropRepo = GenericRepository(CropProduction)
    cropClientRepo = GenericRepository(CropClient)

    def get(self, request, format=None):
        ids=self.cropClientRepo.filterBy("client_id",request.user.client_id,"crop_production_id")
        crop_productions= self.cropRepo.filterBy("crop_production_id__in",ids,None)
        params =[]
        for crop_production in crop_productions:
            if(crop_production):
                serializer = DiseaseSerializer(crop_production.diseases, many = True)
                diseases =[]
                for disease in serializer.data:
                    diseases.append(disease['disease_name'])
                params.append({
                'crop_production':crop_production.crop_production_id,
                'diseases':diseases})
        learningDataAccess = LearningDataAccess()
        response = learningDataAccess.getCurrentRiskRates(params)

        return Response(response)
