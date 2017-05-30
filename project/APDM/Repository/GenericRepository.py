from IGenericRepository import IGenericRepository
from APDM.models import *

class GenericRepository(IGenericRepository):
    genericRepo=None

    @classmethod
    def getInstance(self,classename):
        if(self.genericRepo is None):
            self.genericRepo=GenericRepository(classename)
        return self.genericRepo

    def __init__(self,classname):
        self.classname = classname

    def getAll(self):
        return self.classname.objects.all()

    def getBy(self,field_name,field_value):
        try:
            return self.classname.objects.get(**{field_name: field_value})
        except self.classname.DoesNotExist:
            print "does not exist exception"
            return None

    def filterBy(self, field_name, field_value, column):
        if(column is None):
            return self.classname.objects.filter(**{field_name: field_value})
        else:
            return self.classname.objects.filter(**{field_name: field_value}).values_list(column, flat=True)
