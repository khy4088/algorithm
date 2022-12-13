import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))

start = 0
end = 0
count = 0
result = A[start]

while end < n:
    if result == m:
        count += 1
        end += 1
        if end == n:
            break
        result += A[end]
    elif result < m:
        end += 1
        if end == n:
            break
        result += A[end]
    elif result > m:
        result -= A[start]
        start += 1     
    
print(count)