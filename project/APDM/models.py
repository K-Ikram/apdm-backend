from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'city'
    def __unicode__(self):
        return self.city_name

GENDERCHOICE = (
    ('homme', 'Homme'),
    ('femme', 'Femme'),
)
LANGUAGECHOICE = (
    ('french', 'french'),
    ('english', 'english'),
    ('arabic','arabic'),
    ('spanish','spanish'),
    ('german','german'),
)
class Client(AbstractUser):
    client_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=5, choices=GENDERCHOICE,blank=True, null=True)
    phone_contact = models.CharField(max_length=50,blank=True, null=True,verbose_name='Phone contact')
    phone_sms = models.CharField(max_length=50,blank=True, null=True)
    language = models.CharField(max_length=10, choices=LANGUAGECHOICE,blank=True, null=True)
    notification_sms = models.BooleanField(default=True,help_text="Activicate reception of notifications by SMS")
    notification_email = models.BooleanField(default=True,help_text="Activicate reception of notifications by email")
    comments = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        def __unicode__(self):
            return self.username

class Farm(models.Model):
    farm_id = models.AutoField(primary_key=True)
    farm_name = models.CharField(max_length=50)
    city = models.ForeignKey('City')
    comments = models.CharField(max_length=100, blank=True, null=True)
    clients=models.ManyToManyField(Client, through='Ownfarm')

    class Meta:
        managed = False
        db_table = 'farm'
    def __unicode__(self):
        return self.farm_name

class Ownfarm(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    sensor_type = models.CharField(max_length=20)
    sensor_unit = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sensor'
    def __unicode__(self):
        return self.sensor_type

class Plot(models.Model):
   plot_id = models.AutoField(primary_key=True)
   plot_name = models.CharField(max_length=50)
   latitude_n = models.FloatField()
   longitude_n = models.FloatField()
   latitude_s = models.FloatField()
   longitude_s = models.FloatField()
   soil_type = models.CharField(max_length=10, blank=True, null=True)
   farm = models.ForeignKey('Farm')
   comments = models.CharField(max_length=50, blank=True, null=True)
   sensors = models.ManyToManyField(Sensor, through = 'SensorPlot')

   class Meta:
       managed = False
       db_table = 'plot'
   def __unicode__(self):
       return self.plot_name

class SensorPlot(models.Model):
    plot = models.ForeignKey('Plot',on_delete=models.CASCADE)
    sensor = models.ForeignKey('Sensor',on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

class Crop(models.Model):
    crop_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'crop'

    def __unicode__(self):
        return self.crop_name

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=50)
    crop=models.ForeignKey('Crop',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'disease'
    def __unicode__(self):
        return self.disease_name

class CropProduction(models.Model):
    crop_production_id = models.AutoField(primary_key=True)
    crop = models.ForeignKey('Crop')
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    plot = models.ForeignKey('Plot')
    comments = models.CharField(max_length=100, blank=True, null=True)
    sensors = models.ManyToManyField(Sensor, through = 'CropProductionSensor')
    diseases = models.ManyToManyField(Disease, through = 'CropProductionDisease')

    class Meta:
        managed = False
        db_table = 'crop_production'

    def __unicode__(self):
        return self.name

class CropProductionDisease(models.Model):
    crop_production = models.ForeignKey(CropProduction, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

class CropProductionSensor(models.Model):
    crop_production = models.ForeignKey(CropProduction, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE )

class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alert_date = models.DateTimeField(blank=True, null=True)
    crop_production = models.ForeignKey(CropProduction, on_delete=models.CASCADE)
    risk_rate = models.FloatField(blank=True, null=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    feedback_date = models.DateTimeField(blank=True, null=True)
    feedback_type=models.CharField(max_length=50, blank=True, null=True)

    client = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert'

class Anomaly(models.Model):
    anomaly_id = models.AutoField(primary_key=True)
    occurence_date = models.DateTimeField()
    reporting_date = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    crop_production = models.ForeignKey('CropProduction')
    disease = models.ForeignKey('Disease')

    class Meta:
        managed = False
        db_table = 'anomaly'

class CropClient(models.Model):

    client_id  = models.IntegerField(primary_key = True)
    crop_production_id= models.IntegerField(primary_key = True)

    class Meta:
        managed = False
        db_table = 'crop_client'

class AlertClient(models.Model):

    client  = models.ForeignKey('Client', primary_key = True)
    alert= models.ForeignKey('Alert', primary_key = True)

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
