from ast import stmt
import settings
from cond import Cond
from id import Id
from exp_fac_op import Exp

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
            stmt.parseStmt()
            self.stmts.append(stmt)
            if(self.isStmt()):
                self.parseStmtSeq()
        else:
            print("parseStmtSeq: ERROR token is not apart of a stmt received:", settings.t.token())
    
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
            self.assign.parseAssign()
        elif(token == 'if'):
            self.ifStmt = If()
            self.ifStmt.parseIf()
        elif(token == 'while'):
            self.loop = Loop()
            self.loop.parseLoop()
        elif(token == 'read'):
            self.inStmt = In()
            self.inStmt.parseIn()
        elif(token == 'write'):
            self.out = Out()
            self.out.parseOut()
        else: print("parseStmt: ERROR not able to parse a statement with token:", token)

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
        self.altNo = 1

    def parseIf(self):
        if(settings.t.token() == 'if'):
            settings.t.skipToken()
            self.cond = Cond()
            self.cond.parseCond()
            if(settings.t.token() == 'then'):
                settings.t.skipToken()
                self.stmtSeq1 = StmtSeq()
                self.stmtSeq1.parseStmtSeq()
                if(settings.t.token() == 'else'):
                    self.altNo = 2
                    settings.t.skipToken()
                    self.stmtSeq2 = StmtSeq()
                    self.stmtSeq2.parseStmtSeq()
                    if(settings.t.token() == 'end'):
                        settings.t.skipToken()
                        if(settings.t.token() == ';'):
                            settings.t.skipToken()
                        else: print("parseIf: ERROR expecting ; received", settings.t.token())
                    else: print("parseIf: ERROR expecting end received", settings.t.token())
                elif(settings.t.token() != 'end'):
                    print("parseIf: ERROR expecting end received", settings.t.token())
                else:
                    settings.t.skipToken()
                    if(settings.t.token() != ';'):
                        print("parseIf: ERROR expecting ; received", settings.t.token())
                    else:
                        settings.t.skipToken()
            else: print("parseIf: ERROR expecting then received", settings.t.token())
        else: print("parseIf: ERROR expecting if received", settings.t.token())

    def printIf(self):
        print('if', end='')
        self.cond.printCond()
        print('then')
        self.stmtSeq1.printStmtSeq()
        if(self.altNo == 2):
            print('else')
            self.stmtSeq2.printStmtSeq()
            print('end;')
        else: print('end;')

    def exeIf(self):
        if(self.cond.exeCond()):
            self.stmtSeq1.exeStmtSeq()
        elif(self.altNo == 2):
            self.stmtSeq2()
                
class Loop:

    def __init__(self):
        self.cond = None
        self.stmtSeq = None
    
    def parseLoop(self):
        if(settings.t.token() != 'while'):
            print("parseLoop: ERROR expecting while received", settings.t.token())
        else:
            settings.t.skipToken()
            self.cond = Cond()
            self.cond.parseCond()
            if(settings.t.token() != 'loop'):
                print("parseLoop: ERROR expecting loop received", settings.t.token())
            else:
                settings.t.skipToken()
                self.stmtSeq = StmtSeq()
                self.stmtSeq.parseStmtSeq()
                if(settings.t.token != 'end'):
                    print("parseLoop: ERROR expecting end received", settings.t.token())
                else:
                    if(settings.t.token() != ';'):
                        print("parseLoop: ERROR expecting ; received", settings.t.token())

    def printLoop(self):
        print("while", end='')
        self.cond.printCond()
        print('loop')
        self.stmtSeq.printStmtSeq()
        print('end;')

    def exeLoop(self):
        while(self.cond.exeCond()):
            self.stmtSeq.exeStmtSeq()
    
settings.init('while (A>2) loop\n A = A-1;\nend; ')
loop = Loop()
loop.parseLoop()
loop.printLoop()
