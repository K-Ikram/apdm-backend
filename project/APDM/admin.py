# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
# Register your models here.

SIZE_LISTE_PER_PAGE = 10
SIZE_LISTE_SHOW_ALL = 20

class OwnfarmInline(admin.TabularInline):
    model = Ownfarm
    extra = 1

class CropProductionDiseaseInline(admin.TabularInline):
    model = CropProductionDisease
    extra = 1

class CropProductionSensorInline(admin.TabularInline):
    model = CropProductionSensor
    extra = 1

class SensorPlotInline(admin.TabularInline):
    model = SensorPlot
    extra=1

class PlotAdmin(admin.ModelAdmin):
    list_display =  ['plot_name','soil_type','farm']
    search_fields = ('plot_name',)
    list_filter = ('soil_type','farm',)
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL

class SensorAdmin(admin.ModelAdmin):
    list_display=['sensor_id','sensor_type','sensor_unit','current_plots','associated_crop_productions']
    list_filter = ('sensor_type',)
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    def current_plots(self,obj):
        plots = list(SensorPlot.objects.filter(sensor=obj,end_date=None))
        return ", ".join([plot.plot.plot_name for plot in plots])

    def associated_crop_productions(self,obj):
        crops = list(CropProduction.objects.filter(sensors=obj))
        return ", ".join([crop.name for crop in crops])

    inlines = [SensorPlotInline,CropProductionSensorInline]

class DiseaseAdmin(admin.ModelAdmin):
    list_display=['disease_name','crop','job_period']
    def save_model(self, request, obj, form, change):
        if(not obj.job_period):
            obj.set_job_period(12)
        print "changed job period to",obj.job_period
        obj.save()


class CropProductionAdmin(admin.ModelAdmin):
    list_display=['name','crop','start_date','end_date','yield_field','plot']
    search_fields = ('name',)
    list_filter = ('crop','plot',)
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    inlines=[CropProductionDiseaseInline]

class AlertAdmin(admin.ModelAdmin):
    list_display=['disease','crop_production','risk_rate','alert_date']
    # Remove the delete Admin Action for this Model
    actions = None
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        #Return nothing to make sure user can't update any data
        pass

class AnomalyAdmin(admin.ModelAdmin):
    list_display=['disease','crop_production','occurence_date','reporting_date','client']
    # Remove the delete Admin Action for this Model
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        #Return nothing to make sure user can't update any data
        pass

class ClientAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','gender','date_joined','is_active','is_superuser']
    search_fields = ('username','first_name','last_name','email')
    list_filter = ('gender','language','is_superuser','is_active','groups')
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    fieldsets = (
        (None, {
            'fields': ('username','email','is_staff', 'is_superuser')
        }),
        ('Informations supplémentaires', {
            'classes': ('collapse',),
            'fields': ('first_name','last_name','gender','language',
            'phone_contact','phone_sms','notification_sms','notification_email','groups'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if(not obj.password):
            password = "aitech"+obj.username
            print "password:",password
            obj.set_password(password)
        obj.last_modified_by = request.user
        obj.save()

class FarmAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
    #     qs = super(FarmAdmin, self).get_queryset(request)
    #     if(request.user.is_superuser):
    #         return qs
    #     else:
    #         return qs.filter(clients=request.user.client_id)

    list_display=['farm_name','city' ,'owners']
    search_fields = ('farm_name',)
    list_filter = ('city','clients')
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    inlines = [OwnfarmInline]

    def owners(self, obj):
        return ", ".join([p.username for p in obj.clients.all()])

admin.site.register(Plot, PlotAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(Disease,DiseaseAdmin)
admin.site.register(CropProduction, CropProductionAdmin)
admin.site.register(Alert,AlertAdmin)
admin.site.register(Anomaly,AnomalyAdmin)

admin.site.site_header = 'Panneau d\'administration'
#admin.site.index_title = ''
admin.site.site_title = 'Administration panel'
