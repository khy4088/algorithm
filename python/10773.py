K = int(input())

result = []

for _ in range(K):
    N = int(input())
    if N == 0:
        result = result[:-1]
    else:
        result.append(N)
    
print(sum(result))