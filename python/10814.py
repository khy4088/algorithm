import sys

N = int(input())

names = {}

for _ in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    if age not in names:
        names[age] = [name]
    else:
        names[age].append(name)
        
    
for i in sorted(names.keys()):
    for name in names[i]:
        print(i, name)