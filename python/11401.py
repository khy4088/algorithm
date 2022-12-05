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


N, R = map(int, sys.stdin.readline().rstrip().split())

fact_N = get_fact(N)
fact_K = get_fact(R)
fact_NK = get_fact(N-R)
print(fact_N * devide_pow(fact_K * fact_NK, 1000000005) % 1000000007)