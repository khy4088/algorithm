T = int(input())

def get_pow(n, power):
    if power == 0:
        return 1
    else:
        a = get_pow(n, power // 2)
        a *= a
        a %= 1000000007
        if power % 2:
            return (a * n) % 1000000007
        else:
            return a
        
for _ in range(T):
    N = int(input())
    if N <= 1:
        print(1)
    else:
        print(get_pow(2, N-2))