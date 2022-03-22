# import settings
# from op import Op

# class Fac:
    
#     def __init__(self):
#         self.ops = []
#         self.altNo = 1

#     def parseFac(self):
#         op = Op()
#         op.parseOp()
#         self.ops.append(op)
#         if(settings.t.token() == '*'):
#             settings.t.skipToken()
#             self.altNo = 2
#             self.parseFac()
    
#     def printFac(self):
#         for op in self.ops:
#             op.printOp()
#             if(len(self.ops) - self.ops.index(op) > 1):
#                 print('*', end='')