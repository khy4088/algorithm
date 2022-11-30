import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    stack = []
    temp = False
    if sentence == '.':
        break
    for s in sentence:
        if s == '[':
            stack.append('[')
        elif s == '(':
            stack.append('(')
        elif s == ']':
            if len(stack) == 0:
                temp = True
                break
            elif stack[-1] != '[':
                temp = True
                break
            else:
                del stack[-1]
        elif s == ')':
            if len(stack) == 0:
                temp = True
                break
            elif stack[-1] != '(':
                temp = True
                break
            else:
                del stack[-1]
        else:
            pass
    
    if temp == False and len(stack) !=0:
        temp = True
        
    if temp:
        print('no')
    else:
        print('yes')