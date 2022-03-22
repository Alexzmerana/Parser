# import settings
# from id import Id
# from fac import Exp
# class Op:

#     INT_ID = 31
#     IDEN_ID = 32
#     PAREN_ID = 20
#     def __init__(self):
#         self.id = None
#         self.num = None
#         self.exp = None
        

#     def parseOp(self):
#         self.token = settings.t.getToken()
#         if(self.token == 31):
#             self.num = settings.t.intVal()
#             settings.t.skipToken()
#         elif(self.token == 32):
#             self.id = Id()
#             self.id.parseId()
#         elif(self.token == 20):
#             settings.t.skipToken()
#             self.exp = Exp()
#             self.exp.parseExp()
#             settings.t.skipToken()
#         else:
#             print("parseOp: ERROR received in valide token:", settings.t.token())

#     def printOp(self):
#         if(self.num):
#             print(self.num, end='')
#         elif(self.id):
#             self.id.printId()
#         else:
#             self.exp.printExp()
            

# settings.init()
# settings.t.newLine("()")
# op = Op()
# op.parseOp()
# print(type(1))
# z = type(op)
# print(z)