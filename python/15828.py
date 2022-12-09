import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque(maxlen=N)
while True:
    info = int(input())
    
    if info == -1:
        break
    
    if info == 0:
        queue.popleft()
    elif len(queue) == N:
        pass
    else:
        queue.append(info)

if len(queue) == 0:
    print('empty')
else:
    while queue:
        print(queue.popleft(), end=' ')