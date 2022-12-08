import sys

a = [False] * 20

for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'all':
        a = [True] * 20
    elif cmd[0] == 'empty':
        a = [False] * 20
    else:
        t = int(cmd[1]) - 1
        if cmd[0] == 'add':
            if not(a[t]):
                a[t] = True
        elif cmd[0] == 'remove':
            if a[t]:
                a[t] = False
        elif cmd[0] == 'check':
            if a[t]:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'toggle':
            a[t] = not(a[t])
        del t