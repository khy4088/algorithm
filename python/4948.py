import sys

# N = int(input())
# numbers = list(map(int, sys.stdin.readline().rstrip().split()))

M = 123456 * 2

che = [True] * (M + 1)
count = []
che[1] = False
cnt = 0
for i in range(2, M + 1):
    if che[i] == True:
        for j in range(i + i, M + 1, i):
            che[j] = False


for i in range(len(che)):
    if che[i]:
        cnt += 1
    count.append(cnt)


while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(count[2*n] - count[n])