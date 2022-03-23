import settings
from idlist import IdList

class Decl:

    def __init__(self):
        self.idList = IdList()
        
    def parseDecl(self):
        if(settings.t.token() == 'int'):
            settings.t.skipToken()
            self.idList.parseIdList()
            if(settings.t.token() != ';'):
                print("parseDecl: ERROR expecting \';\' received", settings.t.token())
            else: settings.t.skipToken()
        else:
            print("parseDecl: ERROR expecting \'int\' received", settings.t.token())

    def printDecl(self):
        settings.printTabs()
        print("int ", end='')
        self.idList.printIdList()
        print(';')



# settings.init()
# settings.t.newLine("int A,B,C,D;")
# dec = Decl()
# dec.parseDecl()
# dec.printDecl()
