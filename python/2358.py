from collections import defaultdict

x_cod = defaultdict(list)
y_cod = defaultdict(list)
result = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    x_cod[y].append(x)
    y_cod[x].append(y)
    
for k in x_cod:
    if len(x_cod[k]) >= 2:
        result += 1
        
for k in y_cod:
    if len(y_cod[k]) >= 2:
        result += 1
        
print(result)