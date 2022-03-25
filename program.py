from declseq import DeclSeq
import settings
from declseq import DeclSeq
from stmtseq import StmtSeq
class Program:
    
    def __init__(self):
        self.declSeq = None
        self.stmtSeq = None

    def parseProgram(self):
        if(settings.t.token() == 'program'):
            settings.t.skipToken()
            self.declSeq = DeclSeq()
            self.declSeq.parseDeclSeq()
            if(settings.t.token() == 'begin'):
                settings.t.skipToken()
                self.stmtSeq = StmtSeq()
                if(not self.stmtSeq.parseStmtSeq()): return False
                if(settings.t.token() != 'end'):
                    print("parseProgram: ERROR expecting end received:", settings.t.token())
                    return False
                else: settings.t.skipToken()
            else: 
                print("parseProgram: ERROR expecting begin received", settings.t.token())
                return False
        else: 
            print("parseProgram: ERROR expected program received", settings.t.token())
            return False
        return True

    def printProgram(self):
        print("program")
        settings.s += 1
        self.declSeq.printDeclSeq()
        print("begin")
        self.stmtSeq.printStmtSeq()
        print("end")
    
    def exeProgram(self):
        self.stmtSeq.exeStmtSeq()

    def runProgram(self):
        if(self.parseProgram):
            self.printProgram()
            self.exeProgram()

# settings.init()
# settings.t.newLine("program\nint C12312, A, PP;\nbegin\nC12312=2*2+2*2-3*3-1*A;\nPP=12;\nend")
# program = Program()
# program.parseProgram()
# program.printProgram()