# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^farms/$', FarmList.as_view()),
    url(r'^farm/(?P<pk>[0-9]+)$', FarmDetail.as_view()),

    url(r'^plots/$', PlotList.as_view()),
    url(r'^plots/(?P<pk>[0-9]+)$', PlotDetail.as_view()),
    url(r'^plotsbyfarm/(?P<farm>[0-9]+)$', PlotsByFarm.as_view()),

    url(r'^cropproductions/$', CropProductionList.as_view()),
    url(r'^cropproductions/(?P<pk>[0-9]+)$', CropProductionDetail.as_view()),
    url(r'^cropproductionsbyplot/(?P<plot>[0-9]+)$', CropProductionsByPlot.as_view()),
    url(r'^diseasesbycropproduction/(?P<pk>[0-9]+)$', DiseasesByCropProduction.as_view()),
    url(r'^crop/client/$', CropProductionByClient.as_view()),

    url(r'^disease/(?P<pk>[0-9]+)$', DiseaseDetail.as_view()),

    url(r'^alerts/$', AlertList.as_view()),
    url(r'^alertsbyclient/$', AlertByClient.as_view()),
    url(r'^alertsbycropproduction/(?P<idCropProd>[0-9]+)$', AlertByCropProduction.as_view()),
    url(r'^alerts/(?P<alert_id>[0-9]+)/confirm', ConfirmAlert.as_view()),
    url(r'^alerts/(?P<alert_id>[0-9]+)/deny', DenyAlert.as_view()),
    url(r'^addAnomaly/$', AddAnomaly.as_view()),

    url(r'^disease/(?P<pk>[0-9]+)$', DiseaseDetail.as_view()),
    url(r'^riskrates/(?P<crop>[0-9]+)/(?P<disease>[0-9]+)$', RiskRates.as_view()),
    url(r'^riskratesbycrop/(?P<crop>[0-9]+)$', RiskRateByCrop.as_view()),
    url(r'^currentriskrate/(?P<crop>[0-9]+)/(?P<disease>[0-9]+)$', CurrentRiskRate.as_view()),
    url(r'^maxriskratebyplot/(?P<plot>[0-9]+)$', MaxRiskRateByPlot.as_view()),
    url(r'^maxriskratesbyplot/(?P<plot>[0-9]+)$', MaxRiskRatesByPlot.as_view()),

    url(r'^currentClient/', CurrentClient.as_view()),
    url(r'^updateProfile/(?P<pk>[0-9]+)$', UpdateProfile.as_view()),
    url(r'^changepswd/$', ChangePasswordView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
