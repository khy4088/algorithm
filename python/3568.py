import sys

temp = sys.stdin.readline().rstrip().split()

vartype = temp[0]

for vars in temp[1:]:
    newvar = vartype
    while True:
        if len(vars) == 0:
            break
        elif vars[-1] in ['&', '*']:
            newvar = ''.join([newvar, vars[-1]]) 
            vars = vars[:-1]
        elif vars[-1] == ']':
            newvar = ''.join([newvar, vars[-2:]]) 
            vars = vars[:-2]
        elif vars[-1] == ',':
            vars = vars[:-1]
        elif vars[-1] == ';':
            vars = vars[:-1]
        else:
            break
        
    print(' '.join([newvar, ''.join([vars, ';'])]))  