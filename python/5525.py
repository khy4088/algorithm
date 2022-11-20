import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = str(sys.stdin.readline().rstrip())
P = 'I' + ('OI' * N )
len_P = len(P)
i = 0
count = 0
while True:
    if i+len_P > M:
        break
    if S[i:i+len_P] == P:
        count += 1
    i += 1

print(count)