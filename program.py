from declseq import DeclSeq
import settings
from declseq import DeclSeq
from stmtseq import StmtSeq
class Program:
    
    def __init__(self):
        self.declSeq = DeclSeq()
        self.stmtSeq = StmtSeq()

    def parseProgram(self):
        if(settings.t.token() == 'program'):
            settings.t.skipToken()
            self.declSeq.parseDeclSeq()
            if(settings.t.token() == 'begin'):
                settings.t.skipToken()
                self.stmtSeq.parseStmtSeq()
                if(settings.t.token() != 'end'):
                    print("parseProgram: ERROR expecting end received:", settings.t.token())
            else: print("parseProgram: ERROR expecting begin received", settings.t.token())
        else: print("parseProgram: ERROR expected program received", settings.t.token())

    def printProgram(self):
        print("program")
        print("\t", end='')
        self.declSeq.printDeclSeq()
        print("beign\n\t", end='')
        self.stmtSeq.printStmtSeq()
        print("end")

settings.init()
settings.t.newLine("program\nint C12312, A, PP;\nbegin\nC12312=2*2+2*2-3*3-1*A;\nPP=12;\nend")
program = Program()
program.parseProgram()
program.printProgram()