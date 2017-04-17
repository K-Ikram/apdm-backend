from pymongo import MongoClient
from bson import ObjectId
import datetime
import jsonrpclib
from django.conf import settings

class LearningDataAccess(object):
    learningDataAccess=None

    @classmethod
    def getInstance(self):
        if(self.learningDataAccess is None):
            self.learningDataAccess=LearningDataAccess()
        return self.learningDataAccess

    def __init__(self):
        self.server = jsonrpclib.Server(settings.JSON_RPC_SERVER)

    def getRiskRates(self,crop_production, disease):
        batch = jsonrpclib.MultiCall(self.server)
        batch.getRiskRates(crop_production, disease)
        results = batch()
        for result in results:
            print result
            predictions= result
        #predictions = self.server.getRiskRates(crop_production, disease)
        #print predictions
        return predictions

    def getLastRiskRate(self, crop_production, disease):
        #prediction = self.server.getLastRiskRate(crop_production, disease)
        batch = jsonrpclib.MultiCall(self.server)
        batch.getLastRiskRate(crop_production, disease)
        results = batch()
        for result in results:
            print result
            prediction= result

        return prediction
