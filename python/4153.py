import sys

while True:
    T = list(map(int, sys.stdin.readline().rstrip().split()))
    if T == [0, 0, 0]:
        break
    
    max_value = max(T)
    T.remove(max_value)
    print('right' if max_value**2 == T[0]**2 + T[1]**2 else "wrong")
    
    