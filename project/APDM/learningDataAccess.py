from pymongo import MongoClient
from bson import ObjectId
import datetime
import jsonrpclib
from django.conf import settings

class LearningDataAccess(object):
    learningDataAccess=None

    def __init__(self):
        self.server = jsonrpclib.Server(settings.JSON_RPC_SERVER)

    def getRiskRates(self,crop_production, disease):
        predictions = self.server.getRiskRates(crop_production, disease)
        print predictions
        return predictions

    def getLastRiskRate(self, crop_production, disease):
        prediction = self.server.getLastRiskRate(crop_production, disease)
        return prediction

    def getCurrentRiskRates(self, params):
        response = self.server.getCurrentRiskRates(params)
        return response
