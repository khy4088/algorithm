import sys

def main():
    
    N = int(input())
    num_list = set(map(int, sys.stdin.readline().split()))
    M = int(input())
    find_list = list(map(int, sys.stdin.readline().split()))
    
    for i in find_list:
        if i in num_list:
            print(1)
        else:
            print(0)
        
        
if __name__ == '__main__':
    main()