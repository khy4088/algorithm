import sys

N = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

M = 1000

che = [True] * (M + 1)

che[1] = False

for i in range(2, M + 1):
    if che[i] == True:
        for j in range(i + i, M + 1, i):
            che[j] = False

count = 0

for num in numbers:
    if che[num] == True:
        count += 1
        
print(count)