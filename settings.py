from tokenizer import Tokenizer

def init(data, inputString = ""):
    global t
    t = Tokenizer(inputString)
    global s
    s = 0
    global dataFileName
    dataFileName = data

def printTabs():
    for i in range(s):
        print("\t", end='')
