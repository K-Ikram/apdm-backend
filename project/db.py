# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alert_date = models.DateTimeField()
    crop_production_id = models.IntegerField()
    disease_id = models.IntegerField()
    risk_rate = models.FloatField()
    feedback_date = models.DateTimeField(blank=True, null=True)
    feedback_type = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert'


class Anomaly(models.Model):
    anomaly_id = models.AutoField(primary_key=True)
    occurence_date = models.DateTimeField()
    reporting_date = models.DateTimeField()
    client_id = models.IntegerField()
    crop_production_id = models.IntegerField()
    disease_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anomaly'


class ApdmClient(models.Model):
    client_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=5, blank=True, null=True)
    phone_contact = models.CharField(max_length=50)
    phone_sms = models.CharField(max_length=50)
    language = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField()
    email = models.CharField(max_length=254)
    first_name = models.CharField(max_length=30)
    is_active = models.IntegerField()
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    username = models.CharField(unique=True, max_length=150)
    notification_sms = models.IntegerField()
    notification_email = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apdm_client'


class ApdmClientGroups(models.Model):
    client_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apdm_client_groups'


class ApdmClientUserPermissions(models.Model):
    client_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apdm_client_user_permissions'


class ApdmCropproductiondisease(models.Model):
    crop_production_id = models.IntegerField()
    disease_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apdm_cropproductiondisease'


class ApdmCropproductionsensor(models.Model):
    crop_production_id = models.IntegerField()
    sensor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apdm_cropproductionsensor'


class ApdmOwnfarm(models.Model):
    client_id = models.IntegerField()
    farm_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apdm_ownfarm'


class ApdmSensorplot(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    plot_id = models.IntegerField()
    sensor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apdm_sensorplot'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'city'


class CropProduction(models.Model):
    crop_production_id = models.AutoField(primary_key=True)
    crop = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    plot_id = models.IntegerField()
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crop_production'


class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'disease'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Farm(models.Model):
    farm_id = models.AutoField(primary_key=True)
    farm_name = models.CharField(max_length=50)
    city_id = models.CharField(max_length=50)
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farm'


class Measure(models.Model):
    measure_id = models.AutoField(primary_key=True)
    measure_value = models.FloatField()
    measure_timestamp = models.DateTimeField()
    sensor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'measure'


class Oauth2ProviderAccesstoken(models.Model):
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    application_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderApplication(models.Model):
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True, null=True)
    skip_authorization = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_application'


class Oauth2ProviderGrant(models.Model):
    code = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=255)
    scope = models.TextField()
    application_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderRefreshtoken(models.Model):
    token = models.CharField(unique=True, max_length=255)
    access_token_id = models.IntegerField(unique=True)
    application_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'


class Plot(models.Model):
    plot_id = models.AutoField(primary_key=True)
    plot_name = models.CharField(max_length=50)
    latitude_n = models.FloatField()
    longitude_n = models.FloatField()
    latitude_s = models.FloatField()
    longitude_s = models.FloatField()
    soil_type = models.CharField(max_length=10, blank=True, null=True)
    farm_id = models.IntegerField()
    comments = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plot'


class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    sensor_type = models.CharField(max_length=20)
    sensor_unit = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sensor'
