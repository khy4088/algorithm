import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    distance = y - x
    if distance <= 3:
        print(distance)
    else:
        distance_sqrt = int(distance ** (1/2))
        distance_square = distance_sqrt ** 2
        
        if distance == distance_square:
            print(distance_sqrt * 2 - 1)
        elif distance_sqrt < distance <= distance_sqrt + distance_square:
            print(distance_sqrt * 2)
        elif distance_sqrt + distance_square < distance:
            print(distance_sqrt * 2 + 1)
    