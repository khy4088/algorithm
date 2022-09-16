import sys

def main():
    N = int(input())
    times = []
    for i in range(N):
        times.append(list(map(int, sys.stdin.readline().split())))
    
    times.sort(key = lambda x:x[0])
    times.sort(key = lambda x:x[1])
    
    cnt = 1
    
    end = times[0][1]
    
    for i in range(1, N):
        if times[i][0] >= end:
            cnt += 1
            end = times[i][1]
    
    print(cnt)
    
    
if __name__ == '__main__':
    main()