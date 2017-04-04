from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from models import *
from serializers import *
from rest_framework import permissions
from rest_framework import generics, mixins
import datetime
from oauth2_provider.models import AccessToken, Application
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mongodb import *
import math
class FarmList(generics.ListCreateAPIView):

    def get_farms(self, user):
        try:
            return Farm.objects.filter(clients=user)
        except Farm.DoesNotExist:
            raise Farm.DoesNotExist

    def get(self, request, format=None):
        farms= self.get_farms(user=request.user) # get the farms owned by this user
        serializer = FarmSerializer(farms, many=True)
        return Response(serializer.data)

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

class FarmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

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

    def get(self, request,  idCropProd, format=None):
        alerts = self.get_alert_by_crop_production(idCropProd)
        serializer = AlertSerializer(alerts, many= True)
        return Response(serializer.data)

class UpdateProfile(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ConfirmAlert(generics.RetrieveUpdateAPIView):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = 'alert_id'
    lookup_url_kwarg = 'alert_id'

    dataset_col = TrainingSetCollection()
    prediction_col = PredictionCollection()

    def perform_update(self, serializer):
        serializer.save(client=self.request.user)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.feedback_type = "confirmed"
        instance.feedback_date = datetime.datetime.now().replace(microsecond=0)
        instance.client=request.user
        instance.save()

        # start update training set
        prediction_date = instance.alert_date.replace(minute=0,second=0,microsecond=0)
        prediction = self.prediction_col.getPrediction(instance.crop_production_id,instance.disease.disease_name,prediction_date)
        if prediction is not None:
            if (prediction["disease"] == 1):
                self.dataset_col.addToFHBTrainingSet(prediction)
            else:
                pass # another disease
            rewardNeighbors(self.dataset_col,self.prediction_col,prediction["_id"])
        else:
            print "there is no prediction associated to this confirmed alert"
        # end update training set

        serializer = self.get_serializer(instance,data=instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class DenyAlert(generics.RetrieveUpdateAPIView):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = 'alert_id'
    lookup_url_kwarg = 'alert_id'

    dataset_col = TrainingSetCollection()
    prediction_col = PredictionCollection()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.feedback_type = "denied"
        instance.feedback_date = datetime.datetime.now().replace(microsecond=0)
        instance.client=request.user
        instance.save()

        # start update training set
        prediction_date = instance.alert_date.replace(minute=0,second=0,microsecond=0)
        prediction = self.prediction_col.getPrediction(instance.crop_production_id,instance.disease.disease_name,prediction_date)

        if prediction is not None:
            penalizeNeighbors(self.dataset_col,self.prediction_col,prediction["_id"])
        else:
            print "there is no prediction associated to this declined alert"
        # end update training set

        serializer = self.get_serializer(instance,data=instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class CurrentClient(APIView):
     def get_client(self, user):
        try:
            return Client.objects.get(client_id=user)
        except Client.DoesNotExist:
            raise Client.DoesNotExist

     def get(self, request, format=None):
        client= self.get_client(user=request.user.client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

class AddAnomaly(generics.ListCreateAPIView):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
    dataset_col = TrainingSetCollection()
    prediction_col = PredictionCollection()

    def perform_create(self, serializer):

        serializer.save(client=self.request.user, reporting_date=datetime.datetime.now().replace(microsecond=0) )
        # start update training set
        dt = datetime.datetime.strptime(serializer.data['occurence_date'], '%Y-%m-%dT%H:%M:%SZ')
        disease = Disease.objects.get(pk=serializer.data['disease'])
        print "disease : ",disease
        prediction = self.prediction_col.getPrediction(serializer.data['crop_production'],disease.disease_name,dt)
        if prediction is not None:
            penalizeNeighbors(self.dataset_col,self.prediction_col,prediction["_id"])
        else:
            print "there is no prediction associated to this anomaly"
        # end update training set

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Client
    #permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiskRates(APIView):
    prediction_col = PredictionCollection()
    def get(self, request, crop, disease, format=None):
        disease = Disease.objects.get(pk=disease)
        predictions = self.prediction_col.getRiskRates(int(crop), disease.disease_name)
        serializer = RiskRateSerializer(predictions, many= True)
        return Response(serializer.data)

class RiskRateByCrop(APIView):
    prediction_col = PredictionCollection()

    def get(self, request, crop, format=None):
        crop_production = CropProduction.objects.get(pk=crop)
        # recuperer la liste des maladies surveillees pour cette culture
        serializer = DiseaseSerializer(crop_production.diseases, many = True)
        # disease_number: dn, recuperer le nombre de maladies surveillees
        predictions =[]
        for disease in serializer.data:
            # recuperer les dn predictions les plus recentes de cette culture
            pred = self.prediction_col.getLastRiskRate(int(crop),disease["disease_name"])
            if (pred is not None):
                predictions.append(pred)
        # retourner la liste des predictions
        serializer = RiskRateSerializer(predictions, many= True)
        return Response(serializer.data)

class MaxRiskRateByPlot(APIView):
    prediction_col = PredictionCollection()

    def get(self, request, plot, format=None):
        prediction = None
        maxrisk = 0
        crops = CropProduction.objects.filter(plot=plot)
        predictions =[]
        for crop in crops:
            serializer = DiseaseSerializer(crop.diseases, many = True)
            for disease in serializer.data:
                pred = self.prediction_col.getLastRiskRate(crop.crop_production_id,disease["disease_name"])

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
    prediction_col = PredictionCollection()

    def get(self, request, plot, format=None):
        crops = CropProduction.objects.filter(plot=plot)
        predictions =[]
        for crop in crops:
            prediction = None
            maxrisk = 0
            serializer = DiseaseSerializer(crop.diseases, many = True)
            for disease in serializer.data:
                pred = self.prediction_col.getLastRiskRate(crop.crop_production_id,disease["disease_name"])

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


class CurrentRiskRate(APIView):
    prediction_col = PredictionCollection()
    def get(self, request, crop, disease,format=None):
        prediction = self.prediction_col.getLastRiskRate(int(crop),int(disease))
        serializer = RiskRateSerializer(prediction)
        return Response(serializer.data)

class DiseaseDetail(generics.RetrieveAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class AlertByClient(generics.ListAPIView):

    def get(self, request, format=None):
        try:
            alerts = AlertClient.objects.filter(client =request.user).order_by('alert')
        except AlertClient.DoesNotExist:
            return HttpResponse('not found')

        paginator = Paginator(alerts, 5)
        page = request.GET.get('page')
        print("page",paginator.num_pages)

        try:
            alerts = paginator.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            alerts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver empty array.
            alerts = []
        print(alerts.has_next())
        serializer = AlertClientSerializer(alerts, many=True)

        if alerts.has_previous():
            _previous = alerts.previous_page_number();
        else:
            _previous = None

        if alerts.has_next():
            _next = alerts.next_page_number();
        else:
            _next = None

        return Response({
        "results":serializer.data,
        "count":paginator.num_pages,
        "has_next":alerts.has_next(),
        "has_previous":alerts.has_previous(),
        "previous":_previous,
        "next":_next}
        )

class CropProductionByClient(generics.ListAPIView):

    def get_crop_productions_by_client_ID(self, user):
        try:
            crops=list(CropClient.objects.filter(client=user))
            liste=[]
            for crop in crops:
                 liste.append(crop.crop_production.crop_production_id)
            return list(CropProduction.objects.filter(crop_production_id__in =liste))
        except CropClient.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        crop_productions = self.get_crop_productions_by_client_ID(user=request.user)
        print("==> crops",crop_productions)
        serializer = CropProductionSerializer(crop_productions, many= True)
        return Response(serializer.data)

def rewardNeighbors(dataset_col,prediction_col,prediction_id):
    neighbors = prediction_col.getPredictionNeighbours(prediction_id)
    for neighbor in neighbors:
        old_weight = dataset_col.getTrainingSetElementByID(neighbor)["weight"]
        new_weight = 2- math.pow(old_weight-2,2)/2
        print old_weight, new_weight
        dataset_col.updateTrainingSetElementWeight(neighbor, new_weight)

def penalizeNeighbors(dataset_col,prediction_col,prediction_id):
    neighbors = prediction_col.getPredictionNeighbours(prediction_id)
    for neighbor in neighbors:
        old_weight = dataset_col.getTrainingSetElementByID(neighbor)["weight"]
        new_weight = math.pow(old_weight,2)/2
        print old_weight, new_weight
        dataset_col.updateTrainingSetElementWeight(neighbor, new_weight)
