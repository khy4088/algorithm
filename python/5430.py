import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    inputed = sys.stdin.readline().rstrip()
    if inputed == '[]':
        numbers = deque()
    else:
        numbers = deque(map(str, inputed.lstrip('[').rstrip(']').split(',')))
    reverse = False
    err = False
    for P in p:
        if P == 'R':
            reverse = not(reverse)
        elif P == 'D':
            if len(numbers) == 0:
                err = True
                break
            if reverse:
                numbers.pop()
            else:
                numbers.popleft()
        

    if err:
        answer.append('error')
    else:
        if reverse:
            numbers.reverse()
        result = ','.join(numbers)
        answer.append(f'[{result}]')

for a in answer:
    print(a)