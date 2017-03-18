# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^farms/$', FarmList.as_view()),
    url(r'^farms/(?P<pk>[0-9]+)$', FarmDetail.as_view()),       
    url(r'^farmsbyclient/(?P<client>[0-9]+)$', FarmsByClient.as_view()),
       
    url(r'^plots/$', PlotList.as_view()),
    url(r'^plots/(?P<pk>[0-9]+)$', PlotDetail.as_view()),
    url(r'^plotsbyfarm/(?P<farm>[0-9]+)$', PlotsByFarm.as_view()),
       
    url(r'^cropproductions/$', CropProductionList.as_view()),
    url(r'^cropproductions/(?P<pk>[0-9]+)$', CropProductionDetail.as_view()),
    url(r'^cropproductionsbyplot/(?P<plot>[0-9]+)$', CropProductionsByPlot.as_view()),

    url(r'^diseasesbycropproduction/(?P<pk>[0-9]+)$', DiseasesByCropProduction.as_view()),
       
#    url(r'^riskratesbycropproduction/(?P<pk>[0-9]+)$', RiskRatesByCropProduction.as_view()),
       
]

urlpatterns = format_suffix_patterns(urlpatterns)