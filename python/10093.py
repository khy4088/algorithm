import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

if abs(A-B) == 1:
    print(0)
    exit(0)
elif A==B:
    print(0)
    exit(0)
    
if A > B:
    A, B = B, A

print(B-A-1)

for i in range(A+1,B,1):
    print(i, end = ' ')