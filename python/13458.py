import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

director = 0

for man in A:
    director += 1
    if man-B <= 0:
        continue
    temp = (man-B) % C
    if temp == 0:
        director += (man - B) // C
    else:
        director += (man - B) // C + 1
        
print(director)
