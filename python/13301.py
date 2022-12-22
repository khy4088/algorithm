n = int(input())


dp = [0] * 81
dp[0] = 0
dp[1] = 4
dp[2] = 6
dp[3] = 10
dp[4] = 16

for i in range(5, n+1):
    dp[i] = dp[i-2] + dp[i-1]
    
print(dp[n])