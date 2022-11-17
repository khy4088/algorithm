import sys


N, M = map(int, sys.stdin.readline().split())
pokemon = {}
answer = []
for i in range(N):
    temp_name = input()
    pokemon[temp_name] = i + 1
    pokemon[str(i+1)] = temp_name
    
    
for i in range(M):
    target = input()
    answer.append(pokemon[target])
    
for a in answer:
    print(a)