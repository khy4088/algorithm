import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = str(sys.stdin.readline().rstrip())

i = 0
count = 0
result = 0
while i < M - 1:
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            result += 1
            count -= 1
    
    else:
        i += 1
        count = 0    
        

print(result)