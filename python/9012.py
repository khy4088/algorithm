import sys

T = int(input())

for _ in range(T):
    string = str(sys.stdin.readline().rsplit())
    
    stack = []
    err = False
    for s in string:
        if s == '(':
            stack.append(s)
            # print(stack)
        elif s == ')':
            if not stack:
                # print('ERR')
                err = True
                break
            if stack[-1] == '(':
                stack.pop()
                # print(stack)
        
    if stack or err:
        print('NO')
    elif not stack:
        print('YES')
    # print(stack)