T = int(input())

dp = [0] * 102

for _ in range(T):
    N = int(input())
    for i in range(N+1):
        if i in [0,1,2]:
            dp[i] = 1
        else:
            dp[i] = dp[i-3] + dp[i-2]
    
    print(dp[N-1])