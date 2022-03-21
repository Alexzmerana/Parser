from idlist import IdList
import settings

class Id:
    idDict = {}

    def __init__(self):
        self.id = settings.t.idName()

    def parseId(self):
        Id.idDict[self.id] = 'nil'
        settings.t.skipToken()

    def printId(self):
        print(self.id, end ='')


settings.init()
settings.t.newLine("A1")
print(settings.t.idName())