import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    result = 1
    
    for _ in range(b):
        result *= a
        result %= 10
        
    if result == 0:
        print(10)
    else:
        print(result)