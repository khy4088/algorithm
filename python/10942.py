import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))


result = [[0] * N for _ in range(N)]

for i in range(N):
    for start in range(N - i):
        end = start + i
        if start == end:
            result[start][end] = 1
        elif numbers[start] == numbers[end]:
            if start + 1 == end: 
                result[start][end] = 1
            elif result[start+1][end-1] == 1: 
                result[start][end] = 1

M = int(sys.stdin.readline())

answer = []

for _ in range(M):
    S, E = map(int, input().split())
    answer.append(result[S-1][E-1])

for a in answer:
    print(a)