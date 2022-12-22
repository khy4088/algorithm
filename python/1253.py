import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
a.sort()

count = 0

for i in range(n):
    find = a[i]
    start = 0
    end = n-1
    
    while start < end:
        temp = a[start] + a[end]
        
        if temp == find:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                count += 1
                break
        elif temp < find:
            start += 1
        else:
            end -= 1

print(count)