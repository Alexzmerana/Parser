from ast import stmt
from sre_constants import SUCCESS
import settings
from cond import Cond
from id import Id
from exp_fac_op import Exp
from idlist import IdList

class StmtSeq:
    
    def __init__(self):
        self.stmts = []

    def isStmt(self):
        token = settings.t.token()
        return (settings.t.getToken() == settings.t.IDENTIFIER_ID or token == 'if' or 
            token == 'while' or token == 'read' or token == 'write')
    
    def parseStmtSeq(self):
        
        if(self.isStmt()):
            stmt = Stmt()
            if(not stmt.parseStmt()): return False
            self.stmts.append(stmt)
            if(self.isStmt()):
                if(not self.parseStmtSeq()): return False
            return True
        else:
            print("parseStmtSeq: ERROR token is not apart of a stmt received:", settings.t.token())
            return False
        return True
    
    def printStmtSeq(self):
        for stmt in self.stmts:
            stmt.printStmt()

    def exeStmtSeq(self):
        for stmt in self.stmts:
            stmt.exeStmt()

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
            if(not self.assign.parseAssign()): return False
        elif(token == 'if'):
            self.ifStmt = If()
            if(not self.ifStmt.parseIf()): return False
        elif(token == 'while'):
            self.loop = Loop()
            if(not self.loop.parseLoop()): return False           
        elif(token == 'read'):
            self.inStmt = In()
            if(not self.inStmt.parseIn()): return False            
        elif(token == 'write'):
            self.out = Out()
            if(not self.out.parseOut()): return False          
        else: print("parseStmt: ERROR not able to parse a statement with token:", token)
        return True

    def printStmt(self):
        if(self.assign): self.assign.printAssign()
        elif(self.ifStmt): self.ifStmt.printIf()
        elif(self.loop): self.loop.printLoop()
        elif(self.inStmt): self.inStmt.printIn()
        elif(self.out): self.out.printOut()

    def exeStmt(self):
        if(self.assign): self.assign.exeAssign()
        elif(self.ifStmt): self.ifStmt.exeIf()
        elif(self.loop): self.loop.exeLoop()
        elif(self.inStmt): self.inStmt.exeIn()
        elif(self.out): self.out.exeOut()

class Assign:

    def __init__(self):
        self.id = Id()
        self.exp = Exp()

    def parseAssign(self):
        self.id.parseId()
        if(self.id.isDeclared()):
            if(settings.t.token() == '='):
                settings.t.skipToken()
                if(not self.exp.parseExp()): return False
            else:
                print("parseAssign: ERROR expecting = received:", settings.t.token())
                return False
            if(settings.t.token() != ';'):
                print("parseAssign: ERROR expecting ; received", settings.t.token())
                return False
            else:
                settings.t.skipToken()
        else: 
            print("parseAssign: ERROR id \'", settings.t.token(), "\' not declared", sep='')
            return False
        return True
    
    def printAssign(self):
        settings.printTabs()
        self.id.printId()
        print(' =', end=' ')
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
        self.altNo = 1

    def parseIf(self):
        
        if(settings.t.token() == 'if'):
            settings.t.skipToken()
            self.cond = Cond()
            if(not self.cond.parseCond()): return False
            if(settings.t.token() == 'then'):
                settings.t.skipToken()
                self.stmtSeq1 = StmtSeq()
                if(not self.stmtSeq1.parseStmtSeq()): return False
                if(settings.t.token() == 'else'):
                    self.altNo = 2
                    settings.t.skipToken()
                    self.stmtSeq2 = StmtSeq()
                    if(not self.stmtSeq2.parseStmtSeq()): return False
                    if(settings.t.token() == 'end'):
                        settings.t.skipToken()
                        if(settings.t.token() == ';'):
                            settings.t.skipToken()
                        else: 
                            print("parseIf: ERROR expecting ; received", settings.t.token())
                            return False
                    else: 
                        print("parseIf: ERROR expecting end received", settings.t.token())
                        return False
                elif(settings.t.token() != 'end'):
                    print("parseIf: ERROR expecting end received", settings.t.token())
                    return False
                else:
                    settings.t.skipToken()
                    if(settings.t.token() != ';'):
                        print("parseIf: ERROR expecting ; received", settings.t.token())
                        return False
                    else:
                        settings.t.skipToken()
            else: 
                print("parseIf: ERROR expecting then received", settings.t.token())
                return False
        else: 
            print("parseIf: ERROR expecting if received", settings.t.token())
            return False
        return True

    def printIf(self):
        settings.printTabs()
        print('if ', end='')
        self.cond.printCond()
        print(' then')
        settings.s += 1
        self.stmtSeq1.printStmtSeq()
        settings.s -= 1
        if(self.altNo == 2):
            settings.printTabs()
            print('else')
            settings.s += 1
            self.stmtSeq2.printStmtSeq()
            settings.s -= 1
            settings.printTabs()
            print('end;')
        else: 
            settings.printTabs()
            print('end;')

    def exeIf(self):
        if(self.cond.exeCond()):
            self.stmtSeq1.exeStmtSeq()
        elif(self.altNo == 2):
            self.stmtSeq2.exeStmtSeq()
                
class Loop:

    def __init__(self):
        self.cond = None
        self.stmtSeq = None
    
    def parseLoop(self):
        
        if(settings.t.token() != 'while'):
            print("parseLoop: ERROR expecting while received", settings.t.token())
            return False
        else:
            settings.t.skipToken()
            self.cond = Cond()
            if(not self.cond.parseCond()): return False
            if(settings.t.token() != 'loop'):
                print("parseLoop: ERROR expecting loop received", settings.t.token())
                return False
            else:
                settings.t.skipToken()
                self.stmtSeq = StmtSeq()
                if(not self.stmtSeq.parseStmtSeq()): return False
                if(settings.t.token() != 'end'):
                    print("parseLoop: ERROR expecting end received", settings.t.token())
                    return False
                else:
                    settings.t.skipToken()
                    if(settings.t.token() != ';'):
                        print("parseLoop: ERROR expecting ; received", settings.t.token())
                        return False
                    else: settings.t.skipToken()
        return True
                    

    def printLoop(self):
        settings.printTabs()
        print("while ", end='')
        self.cond.printCond()
        print(' loop')
        settings.s += 1
        self.stmtSeq.printStmtSeq()
        settings.s -= 1
        settings.printTabs()
        print('end;')

    def exeLoop(self):
        while(self.cond.exeCond()):
            self.stmtSeq.exeStmtSeq()
    
class In:
    dataFile = None
    def __init__(self):
        self.idList = None

    def parseIn(self):
        
        if(settings.t.token() != 'read'):
            print("parseIn: ERROR expecting read received", settings.t.token())
            return False
        else:
            In.dataFile = open(settings.dataFileName)
            settings.t.skipToken()
            self.idList = IdList()
            self.idList.parseIdList()
            if(not self.idList.areDeclared()[0]): 
                print("parseIn: ERROR id: ", self.idList.areDeclared()[1], " has not been declared", sep='')
                return False
            if(settings.t.token() != ';'):
                print("parseIn: ERROR expected ; received". settings.t.token())
                return False
            else:
                settings.t.skipToken()
        return True
    
    def printIn(self):
        settings.printTabs()
        print('read ', end='')
        self.idList.printIdList()
        print(';')

    def exeIn(self):
        for id in self.idList.idsList:
            data = In.dataFile.readline()
            if(data):
                id.assignId(int(data))
            else:
                print("exeIn: ERROR nothing to read for id", id.id)
                return

class Out:

    def __init__(self):
        self.idList = None

    def parseOut(self):
        
        if(settings.t.token() != 'write'):
            print("parseOut: ERROR expecting write received", settings.t.token())
            return False
        else:
            settings.t.skipToken()
            self.idList = IdList()
            self.idList.parseIdList()
            if(not self.idList.areDeclared()): 
                print("parseOut: ERROR undeclared id")
                return False
            if(settings.t.token() != ';'):
                print("parseOut: ERROR expecting ; received", settings.t.token())
                return False
            else:
                settings.t.skipToken()
        return True

    def printOut(self):
        settings.printTabs()
        print('write ', end='')
        self.idList.printIdList()
        print(';')

    def exeOut(self):
        for id in self.idList.idsList:
            id.printId()
            print(' = ' , end='')
            print(id.exeId())

# settings.init('while (A>2) loop\n A = A-1;\nend; ')
# loop = Loop()
# loop.parseLoop()
# loop.printLoop()
