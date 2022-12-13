N = int(input())

result = 0.0
remain = N

while remain > 0.0:
    result += N / remain
    remain -= 1
    
print(result)