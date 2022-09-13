from math import floor


def main():
    A, B, C = list(map(int, input().split()))

    if B >= C:
        print("-1")
        exit()
    else:
        print(floor(A/(C-B)+1))
    
if __name__ == '__main__':
    main()