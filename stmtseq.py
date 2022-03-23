import settings
from stmt import Stmt

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
            print()

# settings.init()
# settings.t.newLine("C12312=2*2+2*2-3*3-1*A;\nPP=12;")
# stmtSeq = StmtSeq()
# stmtSeq.parseStmtSeq()
# stmtSeq.printStmtSeq()
