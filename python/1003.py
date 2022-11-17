import sys

# test case 
T = int(sys.stdin.readline().rstrip())


def fibo(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if dp[n] != 0:
        return dp[n]

    dp[n] = fibo(n-1) + fibo(n-2)

    return dp[n]

dp = [0 for _ in range(41)]

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        print('1 0')
        continue
    elif N == 1:
        print('0 1')
    else:
        print(fibo(N-1), fibo(N))