def get_dn(n):
    str_n = str(n)
    temp = 0
    for s_n in str_n:
        temp += int(s_n)
    return n + temp

a = [0] * 10001

for i in range(1, 10001):
    temp = get_dn(i)
    if temp <= 10000:
        a[temp] += 1


for i in range(1, 10001):
    if a[i] == 0:
        print(i)