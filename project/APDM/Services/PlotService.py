from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from APDM.models import *
from APDM.serializers import *
from APDM.Repository.GenericRepository import GenericRepository
from rest_framework import generics, mixins
import datetime
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PlotsByFarm(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    plotRepo = GenericRepository(Plot)

    def get(self, request, farm, format=None):
        plots = self.plotRepo.filterBy("farm",farm,None)
        serializer = PlotSerializer(plots, many= True)
        return Response(serializer.data)

class PlotDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    queryset = GenericRepository(Plot).getAll()
    serializer_class = PlotSerializer
