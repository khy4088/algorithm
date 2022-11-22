import sys

n = int(input())

arr = []


for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    
for i in range(n):
    