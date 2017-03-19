# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^farms/$', FarmList.as_view()),

    url(r'^farm/(?P<pk>[0-9]+)$', FarmDetail.as_view()),       

    url(r'^farms/(?P<pk>[0-9]+)$', FarmDetail.as_view()),       

    url(r'^farmsbyclient/(?P<client>[0-9]+)$', FarmsByClient.as_view()),
       
    url(r'^plots/$', PlotList.as_view()),
    url(r'^plots/(?P<pk>[0-9]+)$', PlotDetail.as_view()),
    url(r'^plotsbyfarm/(?P<farm>[0-9]+)$', PlotsByFarm.as_view()),
       
    url(r'^cropproductions/$', CropProductionList.as_view()),
    url(r'^cropproductions/(?P<pk>[0-9]+)$', CropProductionDetail.as_view()),
    url(r'^cropproductionsbyplot/(?P<plot>[0-9]+)$', CropProductionsByPlot.as_view()),

    url(r'^diseasesbycropproduction/(?P<pk>[0-9]+)$', DiseasesByCropProduction.as_view()),

  
    url(r'^alertsbycropproduction/(?P<idCropProd>[0-9]+)$', AlertByCropProduction.as_view()),
       
#    url(r'^riskratesbycropproduction/(?P<pk>[0-9]+)$', RiskRatesByCropProduction.as_view()),
    url(r'^client/(?P<pk>[0-9]+)$', ClientDetail.as_view()),       
    url(r'^alerts/(?P<alert_id>[0-9]+)/confirm', ConfirmAlert.as_view()),  
    url(r'^alerts/(?P<alert_id>[0-9]+)/deny', DenyAlert.as_view()), 
    url(r'^alerts/$', AlertList.as_view()),       
    url(r'^anomalies/$', AnomalyList.as_view()),       
   

]

urlpatterns = format_suffix_patterns(urlpatterns)