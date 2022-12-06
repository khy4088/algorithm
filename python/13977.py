import sys

def devide_pow(C, n):
    result = 1
    while n:
        if n % 2:
            result *= C % 1000000007
        C *= C
        C %= 1000000007
        n //= 2
    return result % 1000000007


fact = [1] * 4000001
fact[1] = 1

for i in range(2, 4000001):
    fact[i] = i * fact[i-1] % 1000000007

M = int(input())

for _ in range(M):
    N, K = map(int, sys.stdin.readline().rstrip().split())

    print(fact[N] * devide_pow(fact[K] * fact[N-K], 1000000005) % 1000000007)
    
