# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from django import forms
from django.db.models import Count, Min, Max
from django.db.models.functions import Trunc
from django.db.models import DateTimeField
import string
import random
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def password_generator(size=8, chars=string.ascii_uppercase + string.digits+string.lowercase):
	return ''.join(random.choice(chars) for _ in range(size))
# Register your models here.

SIZE_LISTE_PER_PAGE = 10
SIZE_LISTE_SHOW_ALL = 20

class CropProductionDiseaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
		super(CropProductionDiseaseForm, self).__init__(*args, **kwargs)
		print self.fields
		if self.instance:
			try:
				self.fields['disease'].queryset = Disease.objects.filter(crop=self.instance.crop_production.crop)
			except Disease.DoesNotExist:
				pass
    class Meta:
        model = CropProductionDisease
        exclude = []

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
    extra = 0

class PlotInline(admin.TabularInline):
    model = Plot
    verbose_name_plural = "Parcelles associées à cette ferme"
    readonly_fields = ('plot_name','soil_type','comments','latitude','longitude')
    show_change_link=True
    extra = 0
    def has_add_permission(self, request):
        return False

class AddPlotInline(admin.StackedInline):
    verbose_name_plural = "Associer une nouvelle parcelle"
    model = Plot
    fields = ['plot_name','soil_type','comments','latitude','longitude']
    extra = 1
    def has_change_permission(self, request):
        return False

class CropProductionInline(admin.TabularInline):
    model = CropProduction
    verbose_name_plural = "Cultures associées à cette parcelle"
    readonly_fields = ('name','crop','start_date','end_date','yield_field','comments')
    show_change_link=True

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
    list_display =  ['plot_name','soil_type','farm']
    search_fields = ('plot_name',)
    list_filter = ('soil_type','farm',)
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    inlines=[AddCropProductionInline,CropProductionInline]

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
	list_display=['name','crop','start_date','end_date','plot']
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

@admin.register(AnomalySummary)
class AnomalySummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/anomalies_summary__change_list.html'
    date_hierarchy = 'reporting_date'
    list_filter = (
        'crop_production',
    )
    css = {
             'all': ('static/css/summarynew.css',)
        }
    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        response = super(AnomalySummaryAdmin, self).changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('anomaly_id'),

        }

        liste= list(
            qs
            .values('disease')
            .annotate(**metrics)
            .order_by('-total')
        )
        response.context_data['summary']= [{
            'disease': Disease.objects.filter(disease_id=l['disease']).values('disease_name')[0]['disease_name'],
            'total': l['total'] or 0,

        } for l in liste]
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        #print "diseases :",qs.values('disease').annotate(**metrics).order_by('-total')
        summary_over_time = qs.annotate(
            period=Trunc('reporting_date','year',output_field=DateTimeField()),
        ).values('period','disease').annotate(total=Count('anomaly_id')).order_by('period')
        print "summary_over_time", summary_over_time
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        ),

        high = summary_range[0]['high']
        low =0
        print "high :",high
        print "low :",low


        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'disease':Disease.objects.filter(disease_id=x['disease']).values('disease_name')[0]['disease_name'],
            'pct': int(float(x['total'] ) / float(high)* 100)
               if high > low else 0,
            'color': "#4897D8"
                if x['disease']==1 else "#F9A603",

        } for x in summary_over_time]
        return response
FEEDBACKCHOICE={
'confirmed':'Confirmée',
'denied':'Déclinée',
}

@admin.register(AlertSummary)
class AlertSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/alerts_summary__change_list.html'
    date_hierarchy = 'feedback_date'
    list_filter = (
        'disease','crop_production',
    )
    css = {
             'all': ('static/css/summarynew.css',)
        }
    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        response = super(AlertSummaryAdmin, self).changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('alert_id'),

        }

        liste= list(
            qs
            .values('feedback_type','disease')
            .annotate(**metrics)
            .order_by('-total')
        )
        response.context_data['summary']= [{
            'disease': Disease.objects.filter(disease_id=l['disease']).values('disease_name')[0]['disease_name'],
            'feedback_type':FEEDBACKCHOICE.get(l['feedback_type'],'Aucun feedback'),
            'total': l['total'] or 0,

        } for l in liste]


        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        #print "diseases :",qs.values('disease').annotate(**metrics).order_by('-total')
        summary_over_time = qs.filter(feedback_date__isnull=False).annotate(
            period=Trunc('feedback_date','year',output_field=DateTimeField()),
        ).values('period','feedback_type').annotate(total=Count('alert_id')).order_by('period')
        print "summary_over_time", summary_over_time
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        ),

        high = summary_range[0]['high']
        low =0
        print "high :",high
        print "low :",low


        response.context_data['summary_over_time'] = [{
            'period': i['period'],
            'feedback_type': i['feedback_type'],
            'total': i['total'] or 0,
            'pct': int(float(i['total'] ) / float(high)* 100)
               if high > low else 0,
             'color': "#28a717"
                 if i['feedback_type']=="confirmed" else "#f90303",

        } for i in summary_over_time]

        return response

class ClientAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','gender','date_joined','is_active']
    search_fields = ('username','first_name','last_name','email')
    list_filter = ('gender','language','is_superuser','is_active','groups')
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('last_name','first_name','gender','language',
            'phone_contact','phone_sms')
        }),
        ('Informations de compte', {
            'fields': ('username','email','is_staff', 'is_superuser','notification_sms','notification_email','groups')

        }),
    )

    def save_model(self, request, obj, form, change):
        if(not obj.password):
            password = password_generator()
            print "password:",password
            obj.set_password(password)
            subject = u'Bienvenue à la plateforme APDM'
            message = u'Bonjour cher client '+obj.username+u' \nVous pouvez désormais vous connecter à la plateforme APDM en utilisant les informations de connexion suivantes : \nNom d\'utilisateur : '+ obj.username+u'\nMot de passe : '+password+u'\n\n Accéder à la plateforme à partir du lien suivant : http://localhost:4200/login'
            from_addr = 'no-reply@example.com'
            recipient_list = (obj.email,)
            send_mail(subject, message, from_addr, recipient_list,fail_silently=False)

        obj.last_modified_by = request.user
        obj.save()

class FarmAdmin(admin.ModelAdmin):
    list_display=['farm_name','city' ,'proprieraites']
    search_fields = ('farm_name',)
    list_filter = ('city','clients')
    list_per_page = SIZE_LISTE_PER_PAGE
    list_max_show_all = SIZE_LISTE_SHOW_ALL
    inlines = [OwnfarmInline,PlotInline,AddPlotInline]
    fieldsets = (
        ('Informations sur la ferme', {
            'fields': ('farm_name','city','comments')
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
