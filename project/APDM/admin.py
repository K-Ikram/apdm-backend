# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
# Register your models here.

SIZE_LISTE_PER_PAGE = 10
SIZE_LISTE_SHOW_ALL = 20

class CropProductionDiseaseInline(admin.TabularInline):
    model = CropProductionDisease
    classes = ['collapse']
    extra = 1

class CropProductionSensorInline(admin.TabularInline):
    model = CropProductionSensor
    classes = ['collapse']
    extra = 1

class SensorPlotInline(admin.TabularInline):
    model = SensorPlot
    classes = ['collapse']
    extra = 1

class OwnfarmInline(admin.TabularInline):
    model = Ownfarm
    classes = ['collapse']
    extra = 1


class PlotInline(admin.TabularInline):
    model = Plot
    verbose_name_plural = "Parcelles associées à cette ferme"
    readonly_fields = ('plot_name','soil_type','comments','latitude_n','latitude_s','longitude_n','longitude_s')
    show_change_link=True
    extra = 0
    def has_add_permission(self, request):
        return False

class AddPlotInline(admin.StackedInline):
    verbose_name_plural = "Associer une nouvelle parcelle"
    model = Plot
    fields = ['plot_name','soil_type','comments','latitude_n','latitude_s','longitude_n','longitude_s']
    extra = 1
    def has_change_permission(self, request):
        return False


class CropProductionInline(admin.TabularInline):
    model = CropProduction
    verbose_name_plural = "Cultures associées à cette parcelle"
    readonly_fields = ('name','crop','start_date','end_date','yield_field','comments')
    show_change_link=True
    classes = ['collapse']
    extra = 0
    def has_add_permission(self, request):
        return False

class AddCropProductionInline(admin.StackedInline):
    model = CropProduction
    verbose_name_plural = "Associer une nouvelle culture"
    fields = ['name','crop','start_date','end_date','yield_field','comments']
    extra = 1
    classes = ['collapse']
    def has_change_permission(self, request):
        return False

class PlotAdmin(admin.ModelAdmin):
    list_display =  ['plot_name','soil_type','farm','comments']
    search_fields = ('plot_name',)
    list_filter = ('soil_type','farm',)
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    inlines=[CropProductionInline, AddCropProductionInline]

class SensorAdmin(admin.ModelAdmin):
    list_display=['sensor_id','sensor_type','sensor_unit','parcelles_courantes','cultures_associees']
    list_filter = ('sensor_type',)
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    def parcelles_courantes(self,obj):
        plots = list(SensorPlot.objects.filter(sensor=obj,end_date=None))
        return ", ".join([plot.plot.plot_name for plot in plots])

    def cultures_associees(self,obj):
        crops = list(CropProduction.objects.filter(sensors=obj))
        return ", ".join([crop.name for crop in crops])

    inlines = [SensorPlotInline,CropProductionSensorInline]

class CropProductionAdmin(admin.ModelAdmin):
    list_display=['name','crop','start_date','end_date','yield_field','plot']
    search_fields = ('name',)
    list_filter = ('crop','plot',)
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    inlines=[CropProductionDiseaseInline]

class AlertAdmin(admin.ModelAdmin):
    list_display=['disease','crop_production','risk_rate','alert_date']
    readonly_fields = ['disease','crop_production','risk_rate','alert_date','client','feedback_type','feedback_date']
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
    readonly_fields=['disease','crop_production','occurence_date','reporting_date','client']
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

    list_display=['farm_name','city' ,'proprieraites']
    search_fields = ('farm_name',)
    list_filter = ('city','clients')
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    inlines = [OwnfarmInline,PlotInline,AddPlotInline]
    fieldsets = (
        (None, {
            'fields': ('farm_name','city')
        }),
    )

    def proprieraites(self, obj):
        return "\n".join([p.username for p in obj.clients.all()])

admin.site.register(Plot, PlotAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(CropProduction, CropProductionAdmin)
admin.site.register(Alert,AlertAdmin)
admin.site.register(Anomaly,AnomalyAdmin)

admin.site.site_header = 'Panneau d\'administration'
#admin.site.index_title = ''
admin.site.site_title = 'Administration panel'
