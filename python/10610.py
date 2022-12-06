n = input()


try:
    idx = n.index('0')
    a = []
    n = n[0:idx] + n[idx+1:]
    for s in sorted(n, reverse = True):
        a.append(int(s))

    if sum(a) % 3 != 0:
        print(-1)
    else:
        for s in a:
            print(s, end='')
        print(0)
        
except Exception as e:
    print(-1)