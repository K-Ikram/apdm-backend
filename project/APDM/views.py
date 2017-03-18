from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from models import *
from serializers import *
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
class PlotList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  

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

class PlotDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class FarmList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
class FarmDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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

class CropProductionList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    queryset = CropProduction.objects.all()
    serializer_class = CropProductionSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class CropProductionDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    
    queryset = CropProduction.objects.all()
    serializer_class = CropProductionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
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
    
