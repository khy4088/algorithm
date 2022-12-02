from collections import deque

N = int(input())

a = deque([])
for i in range(N):
    a.append(i+1)
    
while len(a) != 1:
    a.popleft()
    a.append(a.popleft())
    
print(a[0])