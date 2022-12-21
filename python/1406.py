import sys
from collections import deque
input = sys.stdin.readline

string_L = deque(input().rstrip())
string_R = deque()

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'L':
        if string_L:
            string_R.appendleft(string_L.pop())
    elif command[0] == 'D':
        if string_R:
            string_L.append(string_R.popleft())
    elif command[0] == 'B':
        if string_L:
            string_L.pop()
    elif command[0] == 'P':
        string_L.append(command[1])
    
    # print('output : ', ''.join(string_L)+''.join(string_R))
    
print(''.join(string_L)+''.join(string_R))
