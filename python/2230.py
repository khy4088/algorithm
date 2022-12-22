import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = []

for _ in range(n):
    A.append(int(input()))

A.sort()

result = 2000000000
start = 0
end = 0

while start < n and end < n:
    diff = abs(A[start] - A[end])
    if m == diff:
        print(m)
        exit()
        
    if m < diff:
        end += 1
    elif diff < m:
        start += 1
    if diff > m:
        result = min(result, diff)
print(result)