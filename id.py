import settings

class Id:
    idDict = {}

    def __init__(self):
        self.id = settings.t.idName()

    def parseId(self):
        if(self.id not in Id.idDict.keys()):
            Id.idDict[self.id] = None
        settings.t.skipToken()

    def printId(self):
        print(self.id, end ='')

    def declared(self):
        return self.id in Id.idDict.keys()
    
    def exeId(self):
        if(self.declared):
            return Id.idDict.get(self.id)
    
    def assignId(self, val):
        Id.idDict[self.id] = val

# settings.init()
# settings.t.newLine("A1")
# print(settings.t.idName())