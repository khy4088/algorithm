import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

num = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = []
prefix_sum.append(num[0])

for i in range(1, N):
    prefix_sum.append(prefix_sum[i-1] + num[i])

a = []
for i in prefix_sum:
    a.append(i % M)

count = [0] * M

for i in a:
    count[i] += 1

result = count[0]

for i in range(M):
    result += (count[i] * (count[i] - 1)) // 2
    
print(result)