import sys

N = int(input())

A = []


for _ in range(N):
    func = list(map(str, sys.stdin.readline().rstrip().split()))
    
    if func[0] == 'push':
        A.append(int(func[1]))
    
    elif func[0] == 'pop':
        if len(A) == 0:
            print(-1)
        
        else:
            print(A[-1])
            del A[-1]

    elif func[0] == 'top':
        if len(A) == 0:
            print(-1)
        else:
            print(A[-1])
            
    elif func[0] == 'size':
        print(len(A))
    
    elif func[0] == 'empty':
        if len(A) == 0:
            print(1)
        else:
            print(0)