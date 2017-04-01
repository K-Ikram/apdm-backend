from pymongo import MongoClient
from bson import ObjectId
import datetime
class MongoConnection(object):

    def __init__(self):
        client = MongoClient('localhost', 8080)
        self.db = client['apdm']

    def get_collection(self, name):
        self.collection = self.db[name]

class TrainingSetCollection(MongoConnection):
    def __init__(self):
       super(TrainingSetCollection, self).__init__()
       self.get_collection('dataset')

    def getTrainingSetElementByID(self,element_id):
        element = self.collection.find_one({"_id":ObjectId(element_id)})
        return element

    def addToFHBTrainingSet(self,prediction):
         result = self.collection.insert_one(
                 {
                 "disease":1,
                 "temp_duration":prediction["temp_duration"],
                 "humidity_avg":prediction["humidity_avg"],
                 "rainfall_duration":prediction["rainfall_duration"],
                 "class":prediction["class"],
                 "weight":1
                 })
         return result

    def updateTrainingSetElementWeight(self,element_id, new_weight):
        result = self.collection.update_one(
                {"_id": element_id},
                {"$set": {"weight":new_weight}})
        return result

class PredictionCollection(MongoConnection):
    def __init__(self):
       super(PredictionCollection, self).__init__()
       self.get_collection('prediction')


    def getPrediction(self,cropProductionID, diseaseName, predictionDate):
        dt = datetime.datetime(predictionDate.year,predictionDate.month,predictionDate.day,predictionDate.hour)
        prediction = self.collection.find_one({"crop_production":cropProductionID,"disease":diseaseName, "prediction_date":dt})
        return prediction

    def getRiskRates(self,cropProductionID, disease):
        predictions = []
        cursor = self.collection.find({"crop_production":cropProductionID, "disease":disease}).sort("prediction_date",-1).limit(10)
        for doc in cursor:
            predictions.append(doc)
        return predictions

    # prediction_date = datetime.datetime(dt.year,dt.month,dt.day)

    def getLastRiskRate(self, crop_production, disease):
        predictions = []
        cursor = self.collection.find({"crop_production":crop_production, "disease":disease}).sort("prediction_date",-1).limit(1)
        return cursor.next()

    def getPredictionByID(self,prediction_id):
        prediction = self.collection.find_one({"_id":ObjectId(prediction_id)})
        return prediction

    def getPredictionNeighbours(self,predictionId):
        neighbors=[]
        prediction = self.collection.find_one({"_id":ObjectId(predictionId)})
        neighbors = prediction["neighbors"]
        return neighbors
