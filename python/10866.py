import sys
input = sys.stdin.readline
from collections import deque
deq = deque()
for _ in range(int(input())):
    query = input().split()
    if query[0] == 'push_back':
        deq.append(int(query[1]))
    elif query[0] == 'push_front':
        deq.appendleft(int(query[1]))
    elif query[0] == 'pop_front':
        print(-1 if len(deq) == 0 else deq.popleft())
    elif query[0] == 'pop_back':
        print(-1 if len(deq) == 0 else deq.pop())
    elif query[0] == 'size':
        print(len(deq))
    elif query[0] == 'empty':
        print(1 if len(deq) == 0 else 0)
    elif query[0] == 'front':
        print(-1 if len(deq) == 0 else deq[0])
    elif query[0] == 'back':
        print(-1 if len(deq) == 0 else deq[-1])
