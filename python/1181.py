N = int(input())

a = {}

for _ in range(N):
    s = input()
    if len(s) in a:
        if s in a[len(s)]:
            continue
        a[len(s)].append(s)
    else:
        a[len(s)] = [s]

for s in sorted(a.keys()):
    for t in sorted(a[s]):
        print(t)