import settings
from id import Id
from exp_fac_op import Exp

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
    
settings.init()
settings.t.newLine("C12312")
id = Id()
id.parseId()
settings.init("C12312=2*2+2*2-3*3-1;")
assign = Assign()
assign.parseAssign()
assign.printAssign()
print(assign.exeAssign())