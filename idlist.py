import settings
from id import Id

class IdList:

    def __init__(self):
        self.idsList = []

    def parseIdList(self):
        newId = Id()
        newId.parseId()
        self.idsList.append(newId)
        if(settings.t.token() == ','):
            settings.t.skipToken()
            self.parseIdList()
    
    def printIdList(self):
        for i in range(len(self.idsList)-1):
            self.idsList[i].printId()
            print(", ", end='')
        self.idsList[i+1].printId()
        
            

# settings.init()
# settings.t.newLine("A,B,C,D")
# idList = IdList()
# idList.parseIdList()
# idList.printIdList()