import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))

start = 0
end = 0
length = n+1
result = A[start]

while end < n:
    if result >= m:
        length = min(end-start+1, length)
        # print(start, end)
        result -= A[start]
        start += 1     
    elif result < m:
        end += 1
        if end == n:
            break
        result += A[end]

if length == n+1:
    print(0)
else:
    print(length)