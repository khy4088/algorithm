N, r = input(), 0
l = len(N)
for i in range(l-1): r+=9*(10**i)*(i+1)
print(r + (int(N)-(10**(l-1))+1)*l)