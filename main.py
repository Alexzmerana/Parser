from http.client import ImproperConnectionState
import settings
from program import Program
import sys

def main():
    progFileName = sys.argv[1]
    progFile = open(progFileName)
    progText = progFile.read()
    settings.init(progText)
    program = Program()
    program.parseProgram()
    program.printProgram()
    program.exeProgram()

main()