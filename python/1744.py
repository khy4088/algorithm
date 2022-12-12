import sys

N = int(sys.stdin.readline())
minus = []
plus = []
zero = False
result = 0
for _ in range(N):
    t = int(sys.stdin.readline())
    if t == 1:
        result += 1
    if t > 1:
        plus.append(t)
    elif t < 0:
        minus.append(t)
    elif t == 0:
        zero = True

plus.sort(reverse=True)
minus.sort()

if zero and len(minus) % 2 == 1:
    del minus[-1]

skip = False

for i in range(len(plus)):
    if skip:
        skip = False
        continue
    elif i == len(plus) - 1:
        result += plus[i]
    else:
        result += plus[i] * plus[i+1]
        skip = True

for i in range(len(minus)):
    if skip:
        skip = False
        continue
    elif i == len(minus) - 1:
        result += minus[i]
    else:
        result += minus[i] * minus[i+1]
        skip = True
        
print(result)