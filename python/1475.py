a = [0] * 9
t = input()
for s in t:
    if s in ['6', '9']:
        a[5] += 1
    else:
        a[int(s)-1] += 1
        
if a[5]%2 == 0:
    a[5] = a[5] // 2
else:
    a[5] = a[5] // 2 + 1
    
print(max(a))