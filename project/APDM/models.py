from __future__ import unicode_literals

from django.db import models

# Create your models here.


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'city'
    def __unicode__(self):
        return self.city_name

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(max_length=50)
    phone_contact = models.CharField(max_length=50)
    phone_sms = models.CharField(max_length=50)
    language = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'client'
    def __unicode__(self):
        return self.name

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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
  

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'disease'
    def __unicode__(self):
        return self.disease_name 
    
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
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    
class CropProduction(models.Model):
    crop_production_id = models.AutoField(primary_key=True)
    crop = models.CharField(max_length=6, blank=True, null=True)
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


#class Measure(models.Model):
#    measure_id = models.AutoField(primary_key=True)
#    measure_value = models.FloatField()
#    measure_timestamp = models.DateTimeField()
#    sensor = models.ForeignKey('Sensor')
#
#    class Meta:
#        managed = False
#        db_table = 'measure'
#        
class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alert_date = models.DateField()
    crop_production = models.ForeignKey('CropProduction')
    risk_rate = models.FloatField()
    disease = models.ForeignKey('Disease')
    feedback_treated = models.IntegerField(blank=True, null=True)
    feedback_date = models.DateField(blank=True, null=True)
    alert_confirmed = models.IntegerField(blank=True, null=True)
    client = models.ForeignKey('Client',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert'
    def __unicode__(self):
        return self.date


class Anomaly(models.Model):
    anomaly_id = models.AutoField(primary_key=True)
    occurence_date = models.DateField()
    reporting_date = models.DateField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    crop_production = models.ForeignKey('CropProduction')
    disease = models.ForeignKey('Disease')
    treated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anomaly'
    def __unicode__(self):
        return self.occurence_date


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FhbPredictions(models.Model):
    prediction_id = models.AutoField(primary_key=True)
    prediction_date = models.DateTimeField()
    crop_production = models.IntegerField()
    temp_duration = models.FloatField()
    humidity_avg = models.FloatField()
    rainfall_duration = models.FloatField()
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    risk_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'fhb_predictions'

    def __unicode__(self):
        return self.prediction_date

