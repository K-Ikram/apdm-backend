class IGenericRepository:

    def __init__(self,classname):
        self.classname = classname

    def getAll(self):
        raise NotImplementedError("get all is not implemented here")

    def filterBy(self,predicate):
        raise NotImplementedError("get all is not implemented here")

    def getByID(self,id):
        raise NotImplementedError("get all is not implemented here")
