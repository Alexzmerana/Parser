from re import S
from tokenizer import Tokenizer

def init(inputString = ""):
    global t
    t = Tokenizer(inputString)
    global s
    s = 0

def printTabs():
    for i in range(s):
        print("\t", end='')