import settings
from id import Id

class Exp:
    
    def __init__(self):
        self.facs = []
        self.altNo = 1
    
    def parseExp(self):
        fac = Fac()
        fac.parseFac()
        self.facs.append(fac)
        if(settings.t.token() == '+' or settings.t.token() == '-'):
            # if(settings.t.token() == '+'): self.altNo = 2
            # else: self.altNo = 3
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
    
    def exeExp(self):
        i = 0
        expVal = self.facs[i].exeFac()
        i += 2
        while(i < len(self.facs)):
            if(self.facs[i-1] == '+'):
                expVal += self.facs[i].exeFac()
            else:
                expVal -= self.facs[i].exeFac()
            i += 2
        return expVal
            

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
            self.parseFac()
    
    def printFac(self):
        for op in self.ops:
            op.printOp()
            if(len(self.ops) - self.ops.index(op) > 1):
                print('*', end='')

    def exeFac(self):
        facVal = 1
        for op in self.ops:
            if(type(op) == type(Op())):
                facVal *= op.exeOp()
        return facVal

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
    
    def exeOp(self):
        if(self.num): return int(self.num)
        elif(self.id): 
            idVal = self.id.exeId()
            if(not idVal): print("exeOp: ERROR id '", self.id.id,"' has no value", sep='')
        else: return self.exp.exeExp()



# settings.init()
# settings.t.newLine("2*2+2*2-3*3-1*3")
# exp = Exp()
# exp.parseExp()
# exp.printExp()
# val = exp.exeExp()
# print('\n',val)
