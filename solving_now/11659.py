import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

a = [0]
temp = 0

for i in num:
    temp += i
    a.append(temp)

# print(a)

for _ in range(M):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    print(a[second] - a[first-1])