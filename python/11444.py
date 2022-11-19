import sys

T = int(sys.stdin.readline().rstrip())

MOD = 1000000007

def square(mat_A, mat_B, mod = 1000000007):
    temp = [[0,0], [0,0]]
    temp[0][0] = (mat_A[0][0] * mat_B[0][0] + mat_A[0][1] * mat_B[1][0]) % mod
    temp[0][1] = (mat_A[0][0] * mat_B[0][1] + mat_A[0][1] * mat_B[1][1]) % mod
    temp[1][0] = (mat_A[1][0] * mat_B[0][0] + mat_A[1][1] * mat_B[1][0]) % mod
    temp[1][1] = (mat_A[1][0] * mat_B[0][1] + mat_A[1][1] * mat_B[1][1]) % mod
    return temp


def fibo_mat(n, mod = 1000000007):
    mat = [[1, 1], [1, 0]]

    if n == 0:
        return [[0, 0], [0, 0]]
    elif n == 1:
        return mat
    
    half_mat = fibo_mat(n//2) # 계산기
    square_mat = square(half_mat, half_mat, mod)
    
    if n % 2:
        return square(square_mat, mat, mod)
    else:
        return square_mat
    
if T == 1:
    print(1)
else:
    print(fibo_mat(T-1, MOD)[0][0] % MOD)