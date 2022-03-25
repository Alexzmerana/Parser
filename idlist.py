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
        for id in self.idsList:
            id.printId()
            if(self.idsList.index(id) + 1 != len(self.idsList)):
                print(", ", end='')

    def areDeclared(self):
        for id in self.idsList:
            if(not id.isDeclared()): 
                return False, id.idName
        return True, id.idName
            
        
            

# settings.init()
# settings.t.newLine("A,B,C,D")
# idList = IdList()
# idList.parseIdList()
# idList.printIdList()