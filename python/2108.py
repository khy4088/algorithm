from collections import Counter
import sys

def main():
    num_list = []
    num = int(sys.stdin.readline())
    for _ in range(num):
        num_list.append(int(sys.stdin.readline()))
        
    num_list.sort()
    length = len(num_list)
    avg = round(sum(num_list) / len(num_list))

    mid = num_list[length // 2]
    cnt = Counter(num_list)

    moco = cnt.most_common()
    if len(moco) > 1:
        if moco[0][1] == moco[1][1]:
            mode = moco[1][0]
        else:
            mode = moco[0][0]
    else:
        mode = moco[0][0]
        
    width = num_list[-1] - num_list[0]

    print(avg)
    print(mid)
    print(mode)
    print(width)
    
    
if __name__ == '__main__':
    main()