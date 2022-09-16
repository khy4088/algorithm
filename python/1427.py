import sys

def main():
    n = str(int(sys.stdin.readline().strip()))
    sorted_n = sorted(n, reverse=True)
    print(''.join(sorted_n))
    
if __name__ == '__main__':
    main()