import sys

def devide_pow(C, n, p):
    if n == 0:
        return 1
    elif n == 1:
        return C % p
    
    result = 1
    
    while n:
        if n % 2:
            result *= C
            result %= p
            
        C *= C
        C %= p
        n //= 2
        
    return result % p

def is_prime(p):
    if p <= 1:
        return False
    elif p  == 2:
        return True
    elif p % 2 == 0:
        return False
    
    for i in range(3, int(p**(1/2)), 2):
        if p % i == 0:
            return False
        
    return True

while True:
    p, a = map(int, sys.stdin.readline().rstrip().split())
    
    if p == 0 and a == 0:
        break  

    if not(is_prime(p)):
        if devide_pow(a, p, p) % p == a:
            print('yes')
        else:
            print('no')
    
    else:
        print('no')