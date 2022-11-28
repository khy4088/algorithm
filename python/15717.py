N = int(input())
R = 1000000007

def get_power(n: int, power: int):
    answer = 1
    while power:
        if power % 2 == True:
            answer = (answer * n) % R
            
        n = n * n % R
        power //= 2
        
    return answer
        
if N <= 1:
    print(1)
else:
    print(get_power(2, N-1))