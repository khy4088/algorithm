N = int(input())


dp = [0] * (N+1)

dp[0] = 1
dp[1] = 3
if N  == 1:
    print(dp[N])
else:
    for i in range(2, N+1):
        dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901
        # print(f'dp[{i}] = {dp[i]}')
        
    print(dp[N])