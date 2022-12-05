import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [[0] * 1001 for _ in range(1001)]



for i in range(N+1):
    for j in range(K+1):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
            
print(dp[N][K] % 10007)