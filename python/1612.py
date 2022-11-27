N = int(input())

if N % 2 == 0 or N % 5 == 0:
    print(-1)

    
else:
    count = 0 
    num = 0
    while True:
        num = num % N
        num = num * 10 + 1
        count += 1
        if num % N == 0:
            break
    print(count)