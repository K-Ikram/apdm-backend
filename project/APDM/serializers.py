# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import *

class DiseaseSerializer(serializers.ModelSerializer):
    crop = serializers.StringRelatedField()
    class Meta:
        model = Disease
        fields = '__all__'

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'

class CropProductionSerializer(serializers.ModelSerializer):
    crop = serializers.StringRelatedField()
    class Meta:
        model = CropProduction
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    #clients = ClientSerializer(many=True)
    class Meta:
        model = Farm

        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    disease = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    crop_production = serializers.StringRelatedField()
    class Meta:
        model = Alert
        fields = '__all__'
        partial=True

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id','gender','phone_contact', 'phone_sms', 'email', 'first_name', 'last_name','username','language','date_joined','is_staff','is_active','is_superuser','last_login','notification_email','notification_sms')

class CropClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropClient
        fields =('client_id','crop_production_id')

class AlertClientSerializer(serializers.ModelSerializer):
    alert_id = AlertSerializer(read_only=True)
    class Meta:
        model = AlertClient
        fields =('alert_id',)

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = '__all__'

class RiskRateSerializer(serializers.Serializer):
    crop_production = serializers.IntegerField()
    disease = serializers.CharField()
    risk_rate= serializers.FloatField()
    prediction_date = serializers.DateTimeField()

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
