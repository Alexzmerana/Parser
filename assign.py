import settings
from id import Id
from exp_fac_op import Exp

class Assign:

    def __init__(self):
        self.id = Id()
        self.exp = Exp()

    def parseAssign(self):
        self.id.parseId()
        if(settings.t.token() == '='):
            settings.t.skipToken()
            self.exp.parseExp()
        else:print("parseAssign: ERROR expecting = received:", settings.t.token())
        if(settings.t.token() != ';'):
            print("parseAssign: ERROR expecting ; received", settings.t.token())
        else:
            settings.t.skipToken()
    
    def printAssign(self):
        self.id.printId()
        print('=', end='')
        self.exp.printExp()
        print(';', end='')
    
# settings.init()
# settings.t.newLine("C12312=2*2+2*2-3*3-1*A;")
# assign = Assign()
# assign.parseAssign()
# assign.printAssign()