import sys

N, B = map(str, sys.stdin.readline().rstrip().split())
B = int(B)

# ord(A) == 65
# so, ALPABET = ord(char) - 65
result = 0
powered = 1
for i in range(len(N)):
    if 10 <= ord(N[-(i+1)]) - 55 <= 35:
        char = ord(N[-(i+1)]) - 55
    else:
        char = int(N[-(i+1)])
    result += char * powered
    powered *= B
    
print(result)