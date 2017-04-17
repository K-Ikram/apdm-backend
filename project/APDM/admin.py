from django.contrib import admin
from .models import *
# Register your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class OwnfarmInline(admin.TabularInline):
    model = Ownfarm
    extra = 1

class CropProductionDiseaseInline(admin.TabularInline):
    model = CropProductionDisease
    extra = 1

class CropProductionSensorInline(admin.TabularInline):
    model = CropProductionSensor
    extra = 1


class ClientAdmin(admin.ModelAdmin):

    list_display=['username','first_name','last_name','email','phone_contact','phone_sms','is_active', 'is_staff', 'is_superuser']
    inlines = [OwnfarmInline]

class FarmAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
    #     qs = super(FarmAdmin, self).get_queryset(request)
    #     if(request.user.is_superuser):
    #         return qs
    #     else:
    #         return qs.filter(clients=request.user.client_id)
    #
    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()

    list_display=['farm_name','city' ,'get_clients']
    inlines = [OwnfarmInline]

    def get_clients(self, obj):
        return "\n".join([p.username for p in obj.clients.all()])

class SensorPlotInline(admin.TabularInline):
    model = SensorPlot

class PlotAdmin(admin.ModelAdmin):
    inlines = [SensorPlotInline]

class SensorAdmin(admin.ModelAdmin):
    inlines = [SensorPlotInline,CropProductionSensorInline]

class DiseaseAdmin(admin.ModelAdmin):
    inlines=(CropProductionDiseaseInline,)

class CropProductionAdmin(admin.ModelAdmin):
    inlines=(CropProductionDiseaseInline,CropProductionSensorInline,)


admin.site.register(Plot, PlotAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(CropProduction, CropProductionAdmin)
admin.site.register(Alert)
admin.site.register(Anomaly)
