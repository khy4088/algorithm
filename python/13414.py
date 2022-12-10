import sys
i = sys.stdin.readline

K, L = map(int, i().split())
q = {}
for _ in range(L):
    n = i().rstrip()
    if n in q:
        del q[n]
        q[n] = None
    else:
        q[n] = None

[print(k) for k in list(q.keys())[:K]]