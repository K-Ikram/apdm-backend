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
    class Meta:
        model = Alert
        fields = '__all__'
        partial=True
#        read_only_fields = ('pk', 'department')



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id','phone_contact', 'phone_sms', 'email', 'first_name', 'last_name','username')
         

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = '__all__'

class RiskRateSerializer(serializers.Serializer):
    crop_production = serializers.IntegerField()
    disease = serializers.IntegerField()
    risk_rate= serializers.FloatField()
    prediction_date = serializers.DateTimeField()

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

