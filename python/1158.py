import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split())

josephus = deque([i+1 for i in range(N)])

# print(josephus)
n = N

start = 0
result = []
for i in range(N):
    # print(start, K, n, (start + K - 1) % n, josephus[(start + K - 1) % n])
    start = (start + K - 1) % n
    n -= 1
    result.append(josephus[start])
    del josephus[start]

print("<" + ", ".join(list(map(str, list(result)))) + ">")