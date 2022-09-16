import sys

def main():
    N, K = list(map(int, sys.stdin.readline().split()))
    money = []
    answer = 0
    for _ in range(N):
        money.append(int(sys.stdin.readline()))
    
    for i in reversed(money):
        if K < i:
            continue
        else:
            answer += K // i
            K %= i
    print(answer)
    
        
if __name__ == '__main__':
    main()