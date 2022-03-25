For this project I made a class for every non-terminal. If I could put them in their own file I did but some have multiple classes in one file
like stmtseq has stmt and everything stmt needs. Every class basically has the same 3 methods parse, print, execute. Some have more like Id
which gives info on whether or not an id has been declared. I think all functions are pretty self explanatory that are not the core three functions.
To execute type the command "py main.py <program file> <data file>" and it should run and print the appropriated error messages. 
As of writing I have not encountered any bugs that prevent this program from running

cond.py - This file has everything need for interpreting cond, (comp and compOp clases)
decl.py - This file has everything need for interpreting decl
declseq.py - This file has everything need for interpreting declseq
exp_fac_op.py - This file has everything need for interpreting exp, fac, and op
id.py - This file has everything need for interpreting id
idlist.py - This file has everything need for interpreting idlist
main.py - This is file contains the main function which sets up the tokenizer and creates a program object and runs it
program.py - This file has everything need for interpreting a program
settings.py - This file has globals that I need like a tokenizer and the name of the data file for read
stmtseq.py - This file has everything need for interpreting stmtseq, stmt, assign, if, loop, in, out
tokenizer.py - Tokenizer object for parsing