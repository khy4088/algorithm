import sys

x, y = map(int, sys.stdin.readline().rstrip().split())
diff = y - x
if diff <= 3:
    print(diff)
else:
    distance_sqrt = int(diff ** (1/2))
    distance_square = distance_sqrt ** 2
    
    if diff == distance_square:
        print(distance_sqrt * 2 - 1)
    elif distance_sqrt < diff <= distance_sqrt + distance_square:
        print(distance_sqrt * 2)
    elif distance_sqrt + distance_square < diff:
        print(distance_sqrt * 2 + 1)
