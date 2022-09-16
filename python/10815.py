import sys

def main():
    N = int(input())
    num_list = set(map(int, sys.stdin.readline().split()))
    M = int(input())
    find_list = list(map(int, sys.stdin.readline().split()))
    a = []
    for i in find_list:
        if i in num_list:
            a.append(str(1))
        else:
            a.append(str(0))
        
    print(' '.join(a))
        
if __name__ == '__main__':
    main()