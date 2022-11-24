import sys

N, K = map(int, sys.stdin.readline().rstrip().split())


N_list = list(range(1, N + 1))
K_list = list(range(1, K + 1))

print(N_list)
print(K_list)

print(N_list[K:])