import settings
from decl import Decl

class DeclSeq:

    def __init__(self):
        self.decl = Decl()

    def parseDeclSeq(self):
        if(settings.t.token() == "int"):
            self.decl.parseDecl()
            if(settings.t.token() == "int"):
                self.parseDeclSeq()
        else:
            print("parseDeclSeq: ERROR expecting \'int\' received", settings.t.token())
    
    def printDeclSeq(self):
        self.decl.printDecl()
    
    def exeDeclSeq(self):
        self.decl.exeDecl()

# settings.init()
# settings.t.newLine("int A,B,C,D;\nint Z;")
# declSeq = DeclSeq()
# declSeq.parseDeclSeq()
# declSeq.printDeclSeq()
