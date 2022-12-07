N = int(input())

X = list(map(int, input().split()))

a = sorted(set(X))
res = {}
for i in range(len(a)):
    res[a[i]] = i

result = []
for i in X:
    result.append(str(res[i]))
    
print(' '.join(result))