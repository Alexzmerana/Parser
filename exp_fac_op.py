import settings
from id import Id

class Exp:
    
    def __init__(self):
        self.facs = []
    
    def parseExp(self):
        fac = Fac()
        fac.parseFac()
        self.facs.append(fac)
        if(settings.t.token() == '+' or settings.t.token() == '-'):
            self.facs.append(settings.t.token())
            settings.t.skipToken()
            self.parseExp()
    
    def printExp(self):
        for fac in self.facs:
            if(fac == '+' or fac == '-'):
                print(fac, end='')
            elif(type(fac) == type(Fac())):
                fac.printFac()
            else: print("printExp: ERROR in valid input:", fac)

class Fac:
    
    def __init__(self):
        self.ops = []
        self.altNo = 1

    def parseFac(self):
        op = Op()
        op.parseOp()
        self.ops.append(op)
        if(settings.t.token() == '*'):
            settings.t.skipToken()
            self.altNo = 2
            self.parseFac()
    
    def printFac(self):
        for op in self.ops:
            op.printOp()
            if(len(self.ops) - self.ops.index(op) > 1):
                print('*', end='')

class Op:

    INT_ID = 31
    IDEN_ID = 32
    PAREN_ID = 20
    def __init__(self):
        self.id = None
        self.num = None
        self.exp = None
        

    def parseOp(self):
        self.token = settings.t.getToken()
        if(self.token == 31):
            self.num = settings.t.intVal()
            settings.t.skipToken()
        elif(self.token == 32):
            self.id = Id()
            self.id.parseId()
        elif(self.token == 20):
            settings.t.skipToken()
            self.exp = Exp()
            self.exp.parseExp()
            settings.t.skipToken()
        else:
            print("parseOp: ERROR received in valide token:", settings.t.token())

    def printOp(self):
        if(self.num):
            print(self.num, end='')
        elif(self.id):
            self.id.printId()
        else:
            self.exp.printExp()


# settings.init()
# settings.t.newLine("2*2+2*2-3*3-1*A")
# exp = Exp()
# exp.parseExp()
# exp.printExp()
