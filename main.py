from http.client import ImproperConnectionState
import settings
from program import Program
import sys

def main():
    progFileName = sys.argv[1]
    dataFile = sys.argv[2]
    progFile = open(progFileName)
    progText = progFile.read()
    settings.init(dataFile, progText)
    program = Program()
    if(program.parseProgram()):
        program.printProgram()
        program.exeProgram()
    else:
        print("ERROR could not parse program")

main()