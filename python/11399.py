import sys

def main():
    N = int(input())
    num_list = list(map(int, sys.stdin.readline().split()))
    total = 0
    t_l = []
    for i in sorted(num_list):
        total += i
        t_l.append(total)
        
    print(sum(t_l))
        
if __name__ == '__main__':
    main()