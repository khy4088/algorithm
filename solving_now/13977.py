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

def get_fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        result %= 1000000007
    return result

M = int(input())

for _ in range(M):
    N, K = map(int, sys.stdin.readline().rstrip().split())

    print(get_fact(N) * devide_pow(get_fact(K) * get_fact(N-K), 1000000005) % 1000000007)
    
