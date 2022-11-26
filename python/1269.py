import sys

len_A, len_b = map(int, sys.stdin.readline().rstrip().split())
A = dict.fromkeys(list(map(int, sys.stdin.readline().rstrip().split())))
B = dict.fromkeys(list(map(int, sys.stdin.readline().rstrip().split())))

count = 0
for key in A.keys():
    if key not in B:
        count +=1

for key in B.keys():
    if key not in A:
        count += 1

print(count)