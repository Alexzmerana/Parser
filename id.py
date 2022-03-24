import settings

class Id:
    idDict = {}

    def __init__(self):
        self.idName = None

    def parseId(self):
        self.idName = settings.t.token()
        settings.t.skipToken()

    def declareId(self):
        if(self.idName not in Id.idDict.keys()):
            Id.idDict[self.idName] = None
        else:
            print("declareId: ERROR id:", self.idName, " is already declared")

    def printId(self):
        print(self.idName, end ='')

    def isDeclared(self):
        return self.idName in Id.idDict.keys()
    
    def isInit(self):
        return Id.idDict[self.idName] != None

    def exeId(self):
        if(self.isInit()):
            return Id.idDict.get(self.idName)
        else:
            print("exeId: ERROR id:", self.idName, " has not been assigned a value")
    
    def assignId(self, val):
        Id.idDict[self.idName] = val

# settings.init()
# settings.t.newLine("A1")
# print(settings.t.idName())