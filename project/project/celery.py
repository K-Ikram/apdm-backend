from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import jsonrpclib
logger = get_task_logger(__name__)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task()
def predireFusarioseBle():
    server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
    results = server.launchDiseaseForecasting(1)
    logger.info("Running FHB Predictor")

@app.task()
def predireMildiouPommeTerre():
    server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
    results = server.launchDiseaseForecasting(2)
    logger.info("Running PLB Predictor")

def trueNegatives(disease_id):
    server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
    server.rewardTrueNegatives()
    logger.info("Running True Negatives")
