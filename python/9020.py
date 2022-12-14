n = int(input())

che = [False, False] + [True] * 10000

for i in range(2, int(10001**0.5)):
    if che[i]:
        for j in range(2*i, 10001, i):
            che[j] = False


for _ in range(n):
    num = int(input())
    
    small = num // 2
    large = num - small
    
    while True:
        if che[small] and che[large]:
            print(small,large)
            break
        small -= 1
        large += 1
    