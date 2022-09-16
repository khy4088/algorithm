import sys
from math import floor

sys.setrecursionlimit(10000)
cnt = 0
K = 0

def merge_sort(A: list, p: int, r: int):
    if (p < r):
        q = floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    
 

def merge(A: list, p: int, q: int, r: int):
    global cnt
    global K
    i = p
    j = q + 1
    t = 1
    
    tmp = [0 for _ in range(len(A)+1)]
    
    while (i <= q and j <= r):
        if (A[i] <= A[j]):
            tmp[t] = A[i]
            t += 1
            i += 1

        else:
            tmp[t] = A[j]
            t += 1
            j += 1

    while(i <= q):
        tmp[t] = A[i]
        t += 1
        i += 1

    
    while(j <= r):
        tmp[t] = A[j]
        t += 1
        j += 1
    
    i = p
    t = 1
    
    while (i <= r):
        A[i] = tmp[t]
        i += 1
        t += 1
        cnt += 1
        if cnt == K:
            print(tmp[t-1])
            exit()
    
    
def main():
    global K
    N, K = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
    merge_sort(A, 0, len(A)-1)
    
if __name__ == '__main__':
    main()
