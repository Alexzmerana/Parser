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
        success = True
        if(self.isStmt()):
            stmt = Stmt()
            if(not stmt.parseStmt()): success = False
            self.stmts.append(stmt)
            if(self.isStmt()):
                if(not self.parseStmtSeq()): success = False
            return True
        else:
            print("parseStmtSeq: ERROR token is not apart of a stmt received:", settings.t.token())
            success = False
        return success
    
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
        success = True
        token = settings.t.token()
        if(settings.t.getToken() == settings.t.IDENTIFIER_ID):
            self.assign = Assign()
            if(not self.assign.parseAssign()): success = False
        elif(token == 'if'):
            self.ifStmt = If()
            if(not self.ifStmt.parseIf()): success = False
        elif(token == 'while'):
            self.loop = Loop()
            if(not self.loop.parseLoop()): success = False           
        elif(token == 'read'):
            self.inStmt = In()
            if(not self.inStmt.parseIn()): success = False            
        elif(token == 'write'):
            self.out = Out()
            if(not self.out.parseOut()): success = False          
        else: print("parseStmt: ERROR not able to parse a statement with token:", token)
        return success

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
        success = True
        if(self.id.isDeclared()):
            self.id.parseId()
            if(settings.t.token() == '='):
                settings.t.skipToken()
                if(not self.exp.parseExp()): success = False
            else:
                print("parseAssign: ERROR expecting = received:", settings.t.token())
                success = False
            if(settings.t.token() != ';'):
                print("parseAssign: ERROR expecting ; received", settings.t.token())
                success = False
            else:
                settings.t.skipToken()
        else: 
            print("parseAssign: ERROR id \'", settings.t.token(), "\' not declared", sep='')
            success = False
        return success
    
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
        success = True
        if(settings.t.token() == 'if'):
            settings.t.skipToken()
            self.cond = Cond()
            self.cond.parseCond()
            if(settings.t.token() == 'then'):
                settings.t.skipToken()
                self.stmtSeq1 = StmtSeq()
                if(not self.stmtSeq1.parseStmtSeq()): success = False
                if(settings.t.token() == 'else'):
                    self.altNo = 2
                    settings.t.skipToken()
                    self.stmtSeq2 = StmtSeq()
                    if(not self.stmtSeq2.parseStmtSeq()): success = False
                    if(settings.t.token() == 'end'):
                        settings.t.skipToken()
                        if(settings.t.token() == ';'):
                            settings.t.skipToken()
                        else: 
                            print("parseIf: ERROR expecting ; received", settings.t.token())
                            success = False
                    else: 
                        print("parseIf: ERROR expecting end received", settings.t.token())
                        success = False
                elif(settings.t.token() != 'end'):
                    print("parseIf: ERROR expecting end received", settings.t.token())
                    success = False
                else:
                    settings.t.skipToken()
                    if(settings.t.token() != ';'):
                        print("parseIf: ERROR expecting ; received", settings.t.token())
                        success = False
                    else:
                        settings.t.skipToken()
            else: 
                print("parseIf: ERROR expecting then received", settings.t.token())
                success = False
        else: 
            print("parseIf: ERROR expecting if received", settings.t.token())
            success = False
        return success

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
        success = True
        if(settings.t.token() != 'while'):
            print("parseLoop: ERROR expecting while received", settings.t.token())
            success = False
        else:
            settings.t.skipToken()
            self.cond = Cond()
            self.cond.parseCond()
            if(settings.t.token() != 'loop'):
                print("parseLoop: ERROR expecting loop received", settings.t.token())
                success = False
            else:
                settings.t.skipToken()
                self.stmtSeq = StmtSeq()
                if(not self.stmtSeq.parseStmtSeq()): success = False
                if(settings.t.token != 'end'):
                    print("parseLoop: ERROR expecting end received", settings.t.token())
                    success = False
                else:
                    if(settings.t.token() != ';'):
                        print("parseLoop: ERROR expecting ; received", settings.t.token())
                        success = False
        return success
                    

    def printLoop(self):
        print("while", end='')
        self.cond.printCond()
        print('loop')
        self.stmtSeq.printStmtSeq()
        print('end;')

    def exeLoop(self):
        while(self.cond.exeCond()):
            self.stmtSeq.exeStmtSeq()
    
class In:

    def __init__(self):
        self.idList = None()

    def parseIn(self):
        success = True
        if(settings.t.token() != 'read'):
            print("parseIn: ERROR expecting read received", settings.t.token())
            success = False
        else:
            settings.t.skipToken()
            self.idList = IdList()
            self.idList.parseIdList()
            if(not self.idList.areDeclared()): success = False
            if(settings.t.token() != ';'):
                print("parseIn: ERROR expected ; received". settings.t.token())
                success = False
            else:
                settings.t.skipToken()
        return success
    
    def printIn(self):
        print('read', end='')
        self.idList.printIdList()
        print(';')

class Out:

    def __init__(self):
        self.idList = None

    def parseOut(self):
        success = True
        if(settings.t.token() != 'write'):
            print("parseOut: ERROR expecting write received", settings.t.token())
            success = False
        else:
            settings.t.skipToken()
            self.idList = IdList()
            self.idList.parseIdList()
            if(not self.idList.areDeclared()): 
                print("parseOut: ERROR undeclared id")
                success = False
            if(settings.t.token() != ';'):
                print("parseOut: ERROR expecting ; received", settings.t.token())
                success = False
            else:
                settings.t.skipToken()
        return success

settings.init('while (A>2) loop\n A = A-1;\nend; ')
loop = Loop()
loop.parseLoop()
loop.printLoop()
