import sys
input = sys.stdin.readline

height = [int(input()) for _ in range(int(input()))]
stack = []
count = 0

for h in height:
    while stack and stack[-1][0] < h:
        count += stack.pop()[1]
        
    if not stack:
        stack.append((h, 1))
        continue
    
    if stack[-1][0] == h:
        temp = stack.pop()[1]
        count += temp
        
        if stack:
            count += 1
        stack.append((h, temp + 1))
    
    else:
        stack.append((h, 1))
        count += 1
        
print(count)