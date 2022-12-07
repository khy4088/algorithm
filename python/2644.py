import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline


def dfs(v):
    for n in E[v]:
        if count[n] == 0:
            count[n] = count[v] + 1
            dfs(n)


n = int(input().rstrip())
visited = [False] * (n+1)
E = [[] for _ in range(n+1)]
count = [0] * (n+1)

first, second = map(int, input().rstrip().split())

m = int(input())

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    E[u].append(v)
    E[v].append(u)
    
dfs(first)

print(count[second] if count[second] != 0 else -1)
