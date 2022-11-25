import sys

N = int(sys.stdin.readline().rstrip())

cards = map(int, sys.stdin.readline().rstrip().split())

count = {}

for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1        


M = int(sys.stdin.readline().rstrip())

nums = map(int, sys.stdin.readline().rstrip().split())
result = []
for num in nums:
    if num in count:
        result.append(str(count[num]))
    else:
        result.append('0')
        
print(' '.join(result))