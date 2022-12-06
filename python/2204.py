import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if not(n):
        break
    temp = []
    for _ in range(n):
        temp.append(sys.stdin.readline().rstrip())
        
    temp.sort(key=str.lower)
    print(temp[0])