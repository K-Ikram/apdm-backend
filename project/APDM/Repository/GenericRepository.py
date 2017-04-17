from IGenericRepository import IGenericRepository
from APDM.models import *
class GenericRepository(IGenericRepository):
    def getAll(self):
        return self.classname.objects.all()

    def getByID(self,pk):
        return self.classname.objects.get(pk=pk)
