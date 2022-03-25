import settings
from id import Id

class Exp:
    
    def __init__(self):
        self.facs = []
        self.altNo = 1
    
    def parseExp(self):
        
        fac = Fac()
        if(not fac.parseFac()): return False
        self.facs.append(fac)
        if(settings.t.token() == '+' or settings.t.token() == '-'):
            self.facs.append(settings.t.token())
            settings.t.skipToken()
            if(not self.parseExp()): return False
        return True
    
    def printExp(self):
        for fac in self.facs:
            if(fac == '+' or fac == '-'):
                print('', fac, end=' ')
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
        if(not op.parseOp()): return False
        self.ops.append(op)
        if(settings.t.token() == '*'):
            settings.t.skipToken()
            if(not self.parseFac()): return False
        return True
    
    def printFac(self):
        for op in self.ops:
            op.printOp()
            if(len(self.ops) - self.ops.index(op) > 1):
                print(' * ', end='')

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
            if(not self.id.isDeclared()):
                print("parseOp: ERROR id:", self.id.idName, " has not been declared")
                return False
        elif(self.token == 20):
            settings.t.skipToken()
            self.exp = Exp()
            self.exp.parseExp()
            settings.t.skipToken()
        else:
            print("parseOp: ERROR received in valide token:", settings.t.token())
            return False
        return True

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
            return self.id.exeId()
        else: return self.exp.exeExp()



# settings.init()
# settings.t.newLine("2*2+2*2-3*3-1*3")
# exp = Exp()
# exp.parseExp()
# exp.printExp()
# val = exp.exeExp()
# print('\n',val)
