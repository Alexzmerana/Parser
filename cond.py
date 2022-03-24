import settings
from exp_fac_op import Op

class CompOp:

    def __init__(self):
        self.compOp = settings.t.token()
        self.altNo = 1

    def parseCompOp(self):
        settings.t.skipToken()
        if(self.compOp == '=='): self.altNo = 2
        elif(self.compOp == '<'): self.altNo = 3
        elif(self.compOp == '>'): self.altNo = 4
        elif(self.compOp == '<='): self.altNo = 5
        else: self.altNo = 6

    def printCompOp(self):
        print(self.compOp, end='')

class Comp:

    def __init__(self):
        self.op1 = None
        self.compOp = None
        self.op2 = None

    def parseComp(self):
        if(settings.t.token() == '('):
            settings.t.skipToken()
            self.op1 = Op()
            self.op1.parseOp()
            self.compOp = CompOp()
            self.compOp.parseCompOp()
            self.op2 = Op()
            self.op2.parseOp()
            if(settings.t.token() != ')'):
                print("parseComp: ERROR expecting ( received", settings.t.token())
            else: settings.t.skipToken()
        else: print("parseComp: ERROR expecting ( received", settings.t.token())

    def printComp(self):
        print('(',end='')
        self.op1.printOp()
        self.compOp.printCompOp()
        self.op2.printOp()
        print(')', end='')
    
    def exeComp(self):
        if(self.compOp.altNo == 1): return (self.op1.exeOp() != self.op2.exeOp())
        elif(self.compOp.altNo == 2): return (self.op1.exeOp() == self.op2.exeOp())
        elif(self.compOp.altNo == 3): return (self.op1.exeOp() < self.op2.exeOp())
        elif(self.compOp.altNo == 4): return (self.op1.exeOp() > self.op2.exeOp())
        elif(self.compOp.altNo == 5): return (self.op1.exeOp() <= self.op2.exeOp())
        elif(self.compOp.altNo == 6): return (self.op1.exeOp() >= self.op2.exeOp())

class Cond:

    def __init__(self):
        self.comp = None
        self.cond1 = None 
        self.cond2 = None
        self.altNo = 1

    def parseCond(self):
        token = settings.t.token()
        if(token == '('): 
            self.comp = Comp()
            self.comp.parseComp()
        elif(token == '!'):
            self.altNo = 2
            self.cond1 = Cond()
            settings.t.skipToken()
            self.cond1.parseCond()
        elif(token == '['):
            settings.t.skipToken()
            self.cond1 = Cond()
            self.cond2 = Cond()
            self.cond1.parseCond()
            if(settings.t.token() == '&&'):
                self.altNo = 3
                settings.t.skipToken()
                self.cond2.parseCond()
                if(settings.t.token() != ']'):
                    print("parseCond: ERROR expected ] received", settings.t.token())
                    return
                else: settings.t.skipToken()
            elif(settings.t.token() == '||'):
                self.altNo = 4
                settings.t.skipToken()
                self.cond2.parseCond()
                if(settings.t.token() != ']'):
                    print("parseCond: ERROR expected ] received", settings.t.token())
                    return
                else: settings.t.skipToken()
            else: 
                print("parseCond: ERROR expected && or || received", settings.t.token())
                return

    def printCond(self):
        if(self.altNo == 1):
            self.comp.printComp()
        elif(self.altNo == 2):
            print('!', end='')
            self.cond1.printCond()
        else:
            print('[',end='')
            self.cond1.printCond()
            if(self.altNo == 3):
                print('&&', end='')
                self.cond2.printCond()
            else:
                print('||', end='')
                self.cond2.printCond()
            print(']', end='')

    def exeCond(self):
        if(self.altNo == 1): return self.comp.exeComp()
        elif(self.altNo == 2): return (not self.cond1.exeCond())
        elif(self.altNo == 3): return (self.cond1.exeCond and self.cond2.exeCond())
        else: return (self.cond1.exeCond() or self.cond2.exeCond())

settings.init("[!(1>1) && [!(1==1) || (2>=2)]]")
cond = Cond()
cond.parseCond()
cond.printCond()
print(cond.exeCond())