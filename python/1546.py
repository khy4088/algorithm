import sys

def main():
    N = list(map(int, sys.stdin.readline().split()))
    score_list = list(map(int, sys.stdin.readline().split()))
    max_score = max(score_list)
    new_score = []
    for score in score_list:
        new_score.append(score / max_score * 100)

    print(sum(new_score) / len(new_score))
    

if __name__ == '__main__':
    main()