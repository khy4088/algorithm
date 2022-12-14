import sys
input = sys.stdin.readline

N = int(input())

work = []
for _ in range(N):
    work.append(list(map(int, input().split())))
    
work = sorted(work, key = lambda x: (x[1], -x[0]))

total_time = 0
max_end = 1000000

for s, e in work:
    total_time += s
    max_end = min(max_end, e-total_time)
    if e < total_time:
        print(-1)
        exit()

print(max_end)