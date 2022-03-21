import sys

class Tokenizer:
    
    RESERVED_TOKENS = ['program', 'begin', 'end', 'int', 'if', 'then', 'else', 'while', 'loop', 'read', 'write', ';',',','=','!','[',']','&&','||','(',')','+','-','*','!=','==','<','>','<=','>=']

    INT_ID = 31
    IDENTIFIER_ID = 32
    MAX_LENGTH_RESERVED_WORD = 7
    EOF_TOKEN = "EOF"
    EOF_ID = 33

    def __init__(self, inputString, debug=False):
        self.inputList = list(inputString)
        self.debug = debug
        self.errorFlag = False
        self.currentToken = self.createTokens()

    def newLine(self, inputString):
        self.inputList = list(inputString)
        self.errorFlag = False
        self.currentToken = self.createTokens()

    def checkforWhiteSpace(self, character):
        if(character.isspace() or not character.isalnum()):
            return True
        else: return False

    def validateWhitespace(self, tempList):
        if(len(tempList) == 0 or self.checkforWhiteSpace(tempList[0])):
            self.inputList = tempList
            return True
        else:
            if(self.debug): print("validateWhitespace: ERROR", tempList[0], "IS NOT WHITESPACE/OP")
            print("Error! Cannot create legal token!")
            self.errorFlag = True
            return False

    def tokenizeOps(self):    
        token = ""
        if len(self.inputList) > 0:
            token = self.inputList.pop(0)
            if(token in Tokenizer.RESERVED_TOKENS):
                if((len(self.inputList) > 0) and (token + self.inputList[0] in Tokenizer.RESERVED_TOKENS)):
                    token += self.inputList.pop(0)
            elif(token + self.inputList[0] in Tokenizer.RESERVED_TOKENS):
                token += self.inputList.pop(0)
            else:
                if(self.debug): print("ERROR", self.inputList[0], "IS NOT A VALID OP")
            if(self.debug): print("tokenizeOps: Created op token:", token)
        return token

    def tokenizeIdentifiers(self):
        if len(self.inputList) > 0:

            if(self.inputList[0].isupper()):

                tempList = self.inputList
                token = tempList.pop(0)

                while(len(tempList) > 0 and (tempList[0].isupper() or tempList[0].isdigit())):
                    token += tempList.pop(0)

                if(self.debug): print("tokenizeIdentifier: Created possible token:", token, "Validating whitespace...")
                validated = self.validateWhitespace(tempList)

                if(validated): 
                    if(self.debug): print("tokenizeIdentifiers: Whitespace validated returning token:", token)
                    return token

            elif(self.debug): print("tokenizeIdentifier: ERROR \"", self.inputList[0], "\" IS NOT AN UPPERCASE CHARACTER")

        else: print("tokenizeIdentifier: ERROR LIST IS EMPTY")

    def tokenizeInts(self):
        tempList = self.inputList

        if(tempList[0].isdigit()):
            token = tempList.pop(0)

            while(len(tempList) > 0 and tempList[0].isdigit()):
                token += tempList.pop(0)

            if(self.debug): print("tokenizeInts: Created possible token:", token, "Validating whitespace...")
            validated = self.validateWhitespace(tempList)

            if(validated):
                if(self.debug): print("tokenizeInts: Whitespace validated returning token:", token)
                return token

        elif(self.debug): print("tokenizeInts: ERROR \"", tempList[0], "\" IS NOT A DIGIT")

    def tokenizeWords(self):
        if(self.inputList[0].islower()):

            for i in range(Tokenizer.MAX_LENGTH_RESERVED_WORD + 1):
                token = ''.join(self.inputList[0:i])

                if(token in Tokenizer.RESERVED_TOKENS):
                    tempList = self.inputList[i:]
                    if(self.debug): print("tokenizeWords: Created possible token:", token, "Validating whitespace...")
                    validated = self.validateWhitespace(tempList)
                    if(validated):
                        if(self.debug): print("tokenizeWords: Whitespace validated returning token:", token)
                        return token


            if(self.debug and not self.errorFlag): print("tokenizeWords: ERROR COULD NOT MAKE TOKEN WITH", self.inputList[0])

    def tokenizeWhitespace(self):
        while(len(self.inputList) > 0 and self.inputList[0].isspace()):
            self.inputList.pop(0)

    def createTokens(self):
        if(len(self.inputList) > 0):
            character = self.inputList[0]

            if(self.debug): print("createTokens: Starting character of token:", character)

            #Reserved words
            if character.islower():
                if(self.debug): print("createTokens: Passing", character, "into tokenizeWords")
                token = self.tokenizeWords()
                if(not self.errorFlag): 
                    if(self.debug): print("createTokens: Received word token:", token)
                    return token
            
            #Identifiers
            elif character.isupper():
                if(self.debug): print("createTokens: Passing", character, "into tokenizeIdentifiers")
                token = self.tokenizeIdentifiers()
                if(not self.errorFlag): 
                    if(self.debug): print("createTokens: Received identifier token:", token)
                    return token

            #Ints
            elif character.isdigit():
                if(self.debug): print("createTokens: Passing", character, "into tokenizeInts")
                token = self.tokenizeInts()
                if(not self.errorFlag): 
                    if(self.debug): print("createTokens: Received int token:", token)
                    return token

            #Whitespace
            elif character.isspace():
                if(self.debug): print("createTokens: Removing whitespace...")
                self.tokenizeWhitespace()
                if(self.debug): print("createTokens: Whitespace removed")
                return self.createTokens()

            #Ops
            else: 
                if(self.debug): print("createTokens: Passing", character, "into tokenizeOps")
                token = self.tokenizeOps()
                if(not self.errorFlag): 
                    if(self.debug): print("createTokens: Received op token:", token)
                    return token
        else: 
            return Tokenizer.EOF_TOKEN

    def sequencer(self, token):
        if token[0].isdigit():
            if self.debug: print("sequencer: Token recognized as int returning", Tokenizer.INT_ID)
            return Tokenizer.INT_ID
        elif token == Tokenizer.EOF_TOKEN:
            if(self.debug): print("sequencer: Token recognized as EOF returning", Tokenizer.EOF_ID)
            return Tokenizer.EOF_ID    
        elif token[0].isupper():
            if self.debug: print("sequencer: Token recognized as an indentifier returning", Tokenizer.IDENTIFIER_ID)
            return Tokenizer.IDENTIFIER_ID
        else:
            if self.debug: print("sequencer: Token recognized as a reserved word looking for index...")
            index = self.RESERVED_TOKENS.index(token) + 1
            if self.debug: print("sequencer: Returning index of", index)
            return index

    def getToken(self):
        if(not self.errorFlag): return self.sequencer(self.currentToken)
    
    def skipToken(self):
        if(not self.errorFlag): 
            token = self.createTokens()
            if(not self.errorFlag): 
                if(self.debug): print("skipToken: Setting current token to", token)
                self.currentToken = token

    def intVal(self):
        if(self.sequencer(self.currentToken) == self.INT_ID):
            return self.currentToken
        
    def idName(self):
        if(self.sequencer(self.currentToken) == self.IDENTIFIER_ID):
            return self.currentToken

    def token(self):
        return self.currentToken
        



