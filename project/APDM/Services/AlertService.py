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
from APDM.mongodb import *
import math
import jsonrpclib
from django.conf import settings

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

class AlertByCropProduction(APIView):

    def get(self, request,  idCropProd, format=None):
        alerts = self.get_alert_by_crop_production(idCropProd)
        serializer = AlertSerializer(alerts, many= True)
        return Response(serializer.data)

class AlertList(generics.ListCreateAPIView):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class ConfirmAlert(generics.RetrieveUpdateAPIView):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = 'alert_id'
    lookup_url_kwarg = 'alert_id'

    def perform_update(self, serializer):
        serializer.save(client=self.request.user)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.feedback_type = "confirmed"
        instance.feedback_date = datetime.datetime.now().replace(microsecond=0)
        instance.client=request.user
        instance.save()

        # start update training set
        dt  =datetime.datetime.strftime(instance.alert_date,'%Y-%m-%dT%H:%M:%SZ')
        server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
        server.reward(dt,instance.disease.disease_name,instance.crop_production.crop_production_id)

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

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.feedback_type = "denied"
        instance.feedback_date = datetime.datetime.now().replace(microsecond=0)
        instance.client=request.user
        instance.save()

        # start update training set
        dt  =datetime.datetime.strftime(instance.alert_date,'%Y-%m-%dT%H:%M:%SZ')
        server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
        server.penalize(dt,instance.disease.disease_name,instance.crop_production.crop_production_id)

        # end update training set

        serializer = self.get_serializer(instance,data=instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
