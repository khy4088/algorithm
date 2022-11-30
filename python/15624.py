import sys

N = int(sys.stdin.readline().rstrip())

if N == 0:
    print('0')
elif N == 1:
    print('1')
else:
    a = 0
    b = 1
    for _ in range(N):
       a, b = b % 1000000007 , a+b % 1000000007
       
    print(a)