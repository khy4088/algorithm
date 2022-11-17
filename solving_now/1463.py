number = int(input())

cnt = 0

while True:
    if number == 1:
        break
    
    if number % 2 == 0:
        number /= 2
    elif number % 3 == 0:
        number /= 3
    else:
        number -= 1
      
    cnt += 1  
    if number == 1:
        break
    

print(cnt)