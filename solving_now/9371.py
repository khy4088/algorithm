import sys

def main():
    TEST_N = int(input())
    for _ in range(TEST_N):
        
        P = int(input())
        
        Ax, Bx, Cx, Kx, Nx = list(map(int, sys.stdin.readline().split()))
        Ay, By, Cy, Ky, Ny = list(map(int, sys.stdin.readline().split())) 
        Fx = []
        Gx = []
        Hx = []
        Fx.append(None)
        Gx.append(None)
        Hx.append(None)
        Fx.append(Ax)
        Gx.append(Bx)
        Hx.append(Cx)
        print(Fx, Gx, Hx)
        for n in range(2, P+1):
            print(n)
            Fx.append(Gx[n-1] + Hx[n-1])
            if n == 2:
                Gx.append(None)
            else:
                Gx.append(Kx * Fx[n-1] + Hx[n-2])
            Hx.append(Fx[n-1] + Kx * Gx[n-1])
        print(Fx, Gx, Hx)

            
if __name__ == '__main__':
    main()