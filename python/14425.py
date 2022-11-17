import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    strings = []
    set_strings = set()
    for _ in range(N):
        set_strings.add(sys.stdin.readline().rstrip())
    for _ in range(M):
        strings.append(sys.stdin.readline().rstrip())
    cnt = 0
    for string in strings:
        if string in set_strings:
            cnt += 1

    print(cnt)
        
if __name__ == '__main__':
    main()