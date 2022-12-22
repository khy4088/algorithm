import sys
input = sys.stdin.readline

n = int(input())

sol = list(map(int, input().split()))
sol.sort()
min = 2000000001
start = 0
end = n - 1
answer = (0,0)

while start < end:
    now = sol[start] + sol[end]
    if abs(now) <= min:
        min = abs(now)
        answer = (sol[start], sol[end])
    
    if now < 0:
        start +=1
    else:
        end -= 1
    
    
print(answer[0], answer[1])