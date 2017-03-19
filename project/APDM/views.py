from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from models import *
from serializers import *
from rest_framework import mixins
from rest_framework import generics
from permissions import IsOwnerOrReadOnly
import datetime



class PlotList(generics.ListCreateAPIView):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    
   
class AlertList(generics.ListCreateAPIView):
    
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

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


   
class FarmList(generics.ListCreateAPIView):

 
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    

 
    
class FarmDetail(generics.RetrieveUpdateDestroyAPIView):

    
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class FarmsByClient(APIView):
    
    def get_farms_by_user_ID(self, client):
        try:
            return list(Farm.objects.filter(clients=client))
        except Farm.DoesNotExist:
            raise Http404

    def get(self, request, client, format=None):
        farms = self.get_farms_by_user_ID(client)
        serializer = FarmSerializer(farms, many= True)
        return Response(serializer.data)


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
    
class RiskRatesByCropProduction(APIView):
    def get_predictions_by_crop_production(self, pk):
        try:
            return list(FhbPredictions.objects.filter(crop_production_id=pk))
        except FhbPredictions.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        predictions = self.get_predictions_by_crop_production(pk)
        
        serializer = PredictionSerializer(predictions, many= True)
        return Response(serializer.data)    


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
    
    
class AlertByCropProduction(APIView):
    
    def get_alert_by_crop_production(self, idCropProd):
        try:
            return list(Alert.objects.filter(crop_production=idCropProd))
        except Alert.DoesNotExist:
            raise Http404

    def get(self, request,  idCropProd, format=None):
        alerts = self.get_alert_by_crop_production(idCropProd)
        serializer = AlertSerializer(alerts, many= True)
        return Response(serializer.data) 
    
class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    


class ConfirmAlert(generics.RetrieveUpdateAPIView):
    
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = 'alert_id'
    lookup_url_kwarg = 'alert_id'
   
    def perform_update(self, serializer):
        serializer.save(client=self.request.user)    

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.alert_confirmed = 1
        instance.feedback_date = datetime.datetime.now().replace(microsecond=0)
        instance.client=request.user
        instance.save()
       
        serializer = self.get_serializer(instance,data=instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)




class DenyAlert(generics.RetrieveUpdateAPIView):
    
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = 'alert_id'
    lookup_url_kwarg = 'alert_id'
   
    def perform_update(self, serializer):
        serializer.save(client=self.request.user) # get the token and its user
       
        

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.alert_denied = 1
        instance.feedback_date = datetime.datetime.now().replace(microsecond=0)
        instance.client=request.user
        instance.save()
       
        serializer = self.get_serializer(instance,data=instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

#class AnomalyList(generics.ListCreateAPIView):
#    queryset = Anomaly.objects.all()
#    serializer_class = AnomalySerializer
#    
#    def post(self, request, *args, **kwargs):
#        
##        instance.alert_denied = 1
##        instance.feedback_date = datetime.datetime.now().replace(microsecond=0)
##        instance.client=request.user
##        instance.save()
#        
#       # instance.occurence_date=request.occurence_date
#        request.reporting_date=datetime.datetime.now().replace(microsecond=0)
##        instance.client=request.user
##        instance.crop_production=request.crop_production
##        instance.disease=request.disease
#        serializer = AnomalySerializer(data=request.data)
#        
#        
#        serializer.is_valid(raise_exception=True)
#        self.perform_update(serializer)
#
#        return Response(serializer.data)
#    
    

    