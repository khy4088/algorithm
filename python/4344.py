import sys

def main():
    N = int(input())
    total_list = []
    for i in range(N):
        score_list = list(map(int, sys.stdin.readline().split()))
        total_list.append(score_list)
        
    for scores in total_list:
        num = scores[0]
        score = scores[1:]
        avg = sum(score) / num
        cnt = 0
        for s in score:
            if s > avg:
                cnt += 1
        avg_p = round(cnt / num * 100, 3)
        print(f'{avg_p:.3f}%')
        
if __name__ == '__main__':
    main()