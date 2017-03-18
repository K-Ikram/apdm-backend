# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import *

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FhbPredictions
        fields = '__all__'

class CropProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropProduction
        fields = '__all__'
        
class FarmSerializer(serializers.ModelSerializer):
    #clients = ClientSerializer(many=True)
    class Meta:
        model = Farm

        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    #clients = ClientSerializer(many=True)
    class Meta:
        model = Alert
        fields = '__all__'



class ClientSerializer(serializers.ModelSerializer):
    #clients = ClientSerializer(many=True)
    class Meta:
        model = Client
        fields = '__all__'







