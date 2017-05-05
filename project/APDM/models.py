# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50,verbose_name="Nom de la ville")

    class Meta:
        verbose_name = 'Ville'
        verbose_name_plural = 'Villes'
        managed = False
        db_table = 'city'
    def __unicode__(self):
        return self.city_name

GENDERCHOICE = (
    ('homme', 'Homme'),
    ('femme', 'Femme'),
)
LANGUAGECHOICE = (
    ('french', 'Français'),
    ('english', 'Anglais'),
    ('arabic','Arabe'),
    ('spanish','Espagnol'),
    ('german','Allmand'),
)
class Client(AbstractUser):
    client_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=5, choices=GENDERCHOICE,blank=True, null=True,verbose_name="genre")
    phone_contact = models.CharField(max_length=50,blank=True, null=True,verbose_name='Tél.')
    phone_sms = models.CharField(max_length=50,blank=True, null=True, verbose_name='Tél. pour la réception des SMS')
    language = models.CharField(max_length=10, choices=LANGUAGECHOICE,blank=True, null=True, verbose_name="Langue")
    notification_sms = models.BooleanField(default=True,verbose_name="Notification par SMS", help_text="Activer ou désativer la reception des notifications par SMS")
    notification_email = models.BooleanField(default=True,verbose_name="Notification par email", help_text="Activer ou désativer la reception des notifications par email")
    comments = models.CharField(max_length=100, blank=True, null=True, verbose_name="Commentaires")
    class Meta:
        managed = False
        db_table = 'apdm_client'
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
        def __unicode__(self):
            return self.username

class Farm(models.Model):
    farm_id = models.AutoField(primary_key=True)
    farm_name = models.CharField(max_length=50,verbose_name="Nom de la ferme")
    city = models.ForeignKey('City', verbose_name="Ville")
    comments = models.CharField(max_length=100, blank=True, null=True, verbose_name="Commentaires")
    clients=models.ManyToManyField(Client, through='Ownfarm', verbose_name="Propriétaires")

    class Meta:
        verbose_name = 'Ferme'
        verbose_name_plural = 'Fermes'
        managed = False
        db_table = 'farm'
    def __unicode__(self):
        return self.farm_name

class Ownfarm(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name="Utilisateur")
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, verbose_name="Ferme")
    class Meta:
        verbose_name = 'Propriétaire'
        verbose_name_plural = 'Propriétaires'

SENSORTYPECHOICE = (
    ('rainfall', 'Précipitations'),
    ('temperature', 'Température'),
    ('humidity','Humidité relative'),
)
class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True, verbose_name="ID du capteur")
    sensor_type = models.CharField(max_length=20, verbose_name="Type du capteur", choices=SENSORTYPECHOICE)
    sensor_unit = models.CharField(max_length=20,verbose_name="Unité de mesure")

    class Meta:
        verbose_name = 'Capteur'
        verbose_name_plural = 'Capteurs'
        managed = False
        db_table = 'sensor'
    def __unicode__(self):
        return self.sensor_type

class Plot(models.Model):
   plot_id = models.AutoField(primary_key=True)
   plot_name = models.CharField(max_length=50, verbose_name="Nom de la parcelle")
   latitude_n = models.FloatField(verbose_name="Lat Nord")
   longitude_n = models.FloatField(verbose_name="Long Nord")
   latitude_s = models.FloatField(verbose_name="Lat Sud")
   longitude_s = models.FloatField(verbose_name="Long Sud")
   soil_type = models.CharField(max_length=10, blank=True, null=True, verbose_name="Type de sol")
   farm = models.ForeignKey('Farm', verbose_name="Ferme")
   comments = models.CharField(max_length=50, blank=True, null=True, verbose_name="Commentaires")
   sensors = models.ManyToManyField(Sensor, through = 'SensorPlot', verbose_name="Capteurs associés")

   class Meta:
        verbose_name = 'Parcelle'
        verbose_name_plural = 'Parcelles'
        managed = False
        db_table = 'plot'
   def __unicode__(self):
        return self.plot_name

class SensorPlot(models.Model):
    plot = models.ForeignKey('Plot',on_delete=models.CASCADE, verbose_name="Parcelle")
    sensor = models.ForeignKey('Sensor',on_delete=models.CASCADE, verbose_name="Capteur")
    start_date = models.DateField(verbose_name="Date de placement du capteur")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date d'enlèvement")
    class Meta:
        verbose_name = 'Parcelle'
        verbose_name_plural = 'Parcelles'

class Crop(models.Model):
    crop_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=50, verbose_name="Type de culture")
    class Meta:
        verbose_name = 'Type de culture'
        verbose_name_plural = 'Types de cultures'
        managed = False
        db_table = 'crop'

    def __unicode__(self):
        return self.crop_name

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=50, verbose_name="Nom de la maladie")
    crop=models.ForeignKey('Crop',on_delete=models.CASCADE, verbose_name="Type de cultures concernées")
    class Meta:
        verbose_name = 'Maladie'
        verbose_name_plural = 'Maladies'
        managed = False
        db_table = 'disease'
    def __unicode__(self):
        return self.disease_name

class CropProduction(models.Model):
    crop_production_id = models.AutoField(primary_key=True)
    crop = models.ForeignKey('Crop', verbose_name="Type de culture")
    name = models.CharField(max_length=50, verbose_name="Nom de la culture")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    yield_field = models.FloatField(db_column='yield', blank=True, null=True,verbose_name="Récolte")  # Field renamed because it was a Python reserved word.
    plot = models.ForeignKey('Plot', verbose_name="Parcelle")
    comments = models.CharField(max_length=100, blank=True, null=True, verbose_name="Commentaires")
    sensors = models.ManyToManyField(Sensor, through = 'CropProductionSensor', verbose_name="Capteurs associés")
    diseases = models.ManyToManyField(Disease, through = 'CropProductionDisease', verbose_name="Maladies surveillées")

    class Meta:
        managed = False
        verbose_name = 'Culture'
        verbose_name_plural = 'Cultures'
        db_table = 'crop_production'

    def __unicode__(self):
        return self.name

class CropProductionDisease(models.Model):
    crop_production = models.ForeignKey(CropProduction, on_delete=models.CASCADE, verbose_name="Culture")
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, verbose_name="Maladie")
    class Meta:
        verbose_name = 'Maladie'
        verbose_name_plural = 'Maladies sureillées'

class CropProductionSensor(models.Model):
    crop_production = models.ForeignKey(CropProduction, on_delete=models.CASCADE,verbose_name="Culture")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name="Capteur" )
    class Meta:
        verbose_name = 'Culture'
        verbose_name_plural = 'Cultures'

class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    crop_production = models.ForeignKey(CropProduction, on_delete=models.CASCADE, verbose_name="Culture concernée")
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, verbose_name="Maladie")
    risk_rate = models.FloatField(blank=True, null=True, verbose_name="Taux de risque")
    alert_date = models.DateTimeField(blank=True, null=True, verbose_name="Date de l'alerte")
    feedback_type=models.CharField(max_length=50, blank=True, null=True, verbose_name="Type de feebdback")
    client = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,verbose_name="Source du feedback")
    feedback_date = models.DateTimeField(blank=True, null=True, verbose_name="Date du feedback")

    class Meta:
        verbose_name = 'Alerte'
        verbose_name_plural = 'Alertes'
        managed = False
        db_table = 'alert'

class Anomaly(models.Model):
    anomaly_id = models.AutoField(primary_key=True)
    occurence_date = models.DateTimeField(verbose_name="Date d'occurrence")
    disease = models.ForeignKey('Disease', verbose_name="Type de la maladie")
    crop_production = models.ForeignKey('CropProduction', verbose_name="Culture concernée")
    reporting_date = models.DateTimeField(blank=True, null=True, verbose_name="Date de signalisation")
    client = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,verbose_name="Signalé par")

    class Meta:
        verbose_name = 'Anomalie'
        verbose_name_plural = 'Anomalies'
        managed = False
        db_table = 'anomaly'

class CropClient(models.Model):

    client_id  = models.IntegerField(primary_key = True)
    crop_production_id= models.IntegerField(primary_key = True)

    class Meta:
        managed = False
        db_table = 'crop_client'

class AlertClient(models.Model):

    client_id  = models.IntegerField(primary_key = True)
    alert_id= models.IntegerField(primary_key = True)

    class Meta:
        managed = False
        db_table = 'alert_client'

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
