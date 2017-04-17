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
from APDM.learningDataAccess import *
import math

class RiskRates(APIView):
    learningDataAccess = LearningDataAccess.getInstance()
    def get(self, request, crop, disease, format=None):
        disease = Disease.objects.get(pk=disease)
        predictions = self.learningDataAccess.getRiskRates(int(crop), disease.disease_name)
        serializer = RiskRateSerializer(predictions, many= True)
        return Response(serializer.data)
import jsonrpclib
from django.conf import settings

class RiskRateByCrop(APIView):
    learningDataAccess = LearningDataAccess.getInstance()
    #server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
    def get(self, request, crop, format=None):
        crop_production = CropProduction.objects.get(pk=crop)
        # recuperer la liste des maladies surveillees pour cette culture
        serializer = DiseaseSerializer(crop_production.diseases, many = True)
        # disease_number: dn, recuperer le nombre de maladies surveillees
        predictions =[]
        #batch = jsonrpclib.MultiCall(self.server)

        for disease in serializer.data:
            # recuperer les dn predictions les plus recentes de cette culture
            pred = self.learningDataAccess.getLastRiskRate(int(crop),disease["disease_name"])
            #batch.getLastRiskRate(int(crop),disease["disease_name"])

            if (pred is not None):
                predictions.append(pred)
        # predictions = batch()
        # retourner la liste des predictions
        serializer = RiskRateSerializer(predictions, many= True)
        return Response(serializer.data)

class MaxRiskRateByPlot(APIView):
    learningDataAccess = LearningDataAccess.getInstance()

    def get(self, request, plot, format=None):
        prediction = None
        maxrisk = 0
        crops = CropProduction.objects.filter(plot=plot)
        predictions =[]
        for crop in crops:
            serializer = DiseaseSerializer(crop.diseases, many = True)
            for disease in serializer.data:
                pred = self.learningDataAccess.getLastRiskRate(crop.crop_production_id,disease["disease_name"])

                if pred is not None:
                    if(maxrisk<pred['risk_rate']):
                        maxrisk = pred['risk_rate']
                        prediction = pred
                else:
                    print "there is no prediction"

        if prediction is None:
            return HttpResponse("No prediction")
        serializer = RiskRateSerializer(prediction)
        return Response(serializer.data)

class MaxRiskRatesByPlot(APIView):
    learningDataAccess = LearningDataAccess.getInstance()

    def get(self, request, plot, format=None):
        crops = CropProduction.objects.filter(plot=plot)
        predictions =[]
        for crop in crops:
            prediction = None
            maxrisk = 0
            serializer = DiseaseSerializer(crop.diseases, many = True)
            for disease in serializer.data:
                pred = self.learningDataAccess.getLastRiskRate(crop.crop_production_id,disease["disease_name"])

                if pred is not None:
                    if(maxrisk<pred['risk_rate']):
                        maxrisk = pred['risk_rate']
                        prediction = pred
                else:
                    print "there is no prediction"
            if prediction is not None:
                predictions.append(prediction)


        serializer = RiskRateSerializer(predictions,many=True)
        return Response(serializer.data)
