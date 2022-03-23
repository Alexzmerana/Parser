import settings
from assign import Assign

class Stmt:
    
    def __init__(self):
        self.assign = Assign()

    def parseStmt(self):
        self.assign.parseAssign()

    def printStmt(self):
        self.assign.printAssign()
    
# settings.init()
# settings.t.newLine("C12312=2*2+2*2-3*3-1*A;")
# stmt = Stmt()
# stmt.parseStmt()
# stmt.printStmt()