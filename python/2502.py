import sys

D, K = map(int, sys.stdin.readline().split())

dp = [0] * (D+1)
dp[1] = 1
dp[2] = 1
for i in range(3,D+1):
    dp[i] = dp[i-2] + dp[i-1]

A = dp[D-2]
B = dp[D-1]
one = 1
two = 1

while True:
    if one*dp[D-2] + two*dp[D-1] == K:
        print(one, two, sep='\n')
        break
    elif one*dp[D-2] + two*dp[D-1] < K:
        two += 1
    else:
        one += 1
        two = 1