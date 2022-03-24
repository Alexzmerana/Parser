import settings
from assign import Assign
from cond import Cond
from id import Id
from exp_fac_op import Exp
class Stmt:
    
    def __init__(self):
        self.assign = None
        self.ifStmt = None
        self.loop = None
        self.inStmt = None
        self.out = None

    def parseStmt(self):
        token = settings.t.token()
        if(settings.t.getToken() == settings.t.IDENTIFIER_ID):
            self.assign = Assign()
        # elif(token = 'if'):
        #     self.ifStmt = If()
        #     self.ifStmt.parseIf()
        # elif(token == 'while'):
        #     self.loop = Loop()
        #     self.loop.parseLoop()
        # elif(token == 'read'):
        #     self.inStmt = In()
        #     self.inStmt.parseIn()
        # elif(token == 'write'):
        #     self.out = Out()
        #     self.out.parseOut()
        else: print("parseStmt: ERROR not able to parse a statement with token:", token)

    def printStmt(self):
        if(self.assign): self.assign.exeAssign()
        # elif(self.ifStmt): self.ifStmt.printIf()
        # elif(self.loop): self.loop.printLoop()
        # elif(self.inStmt): self.inStmt.printIn()
        # elif(self.out): self.out.printOut()

    def exeStmt(self):
        if(self.assign): self.assign.exeAssign()
        # elif(self.ifStmt): self.ifStmt.exeIf()
        # elif(self.loop): self.loop.exeLoop()
        # elif(self.inStmt): self.inStmt.exeIn()
        # elif(self.out): self.out.exeOut()
    

class Assign:

    def __init__(self):
        self.id = Id()
        self.exp = Exp()

    def parseAssign(self):
        if(self.id.declared()):
            self.id.parseId()
            if(settings.t.token() == '='):
                settings.t.skipToken()
                self.exp.parseExp()
            else:print("parseAssign: ERROR expecting = received:", settings.t.token())
            if(settings.t.token() != ';'):
                print("parseAssign: ERROR expecting ; received", settings.t.token())
            else:
                settings.t.skipToken()
        else: print("parseAssign: ERROR id \'", settings.t.token(), "\' not declared", sep='')
    
    def printAssign(self):
        settings.printTabs()
        self.id.printId()
        print('=', end='')
        self.exp.printExp()
        print(';')
    
    def exeAssign(self):
        val = self.exp.exeExp()
        self.id.assignId(val)
        return self.id.exeId()
class If:

    def __init__(self):
        self.cond = None
        self.stmtSeq1 = None 
        self.stmtSeq2 = None

    def parseIf(self):
        if(settings.t.token() == 'if'):
            settings.t.skipToken()
            self.cond = Cond()
            self.cond.parseCond()

# settings.init()
# settings.t.newLine("C12312=2*2+2*2-3*3-1*A;")
# stmt = Stmt()
# stmt.parseStmt()
# stmt.printStmt()