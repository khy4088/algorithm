from itertools import combinations

def main():
    sub = 1e10
    _, target = list(map(int, input().split()))
    card = list(map(int, input().split()))
    for case in combinations(card, 3):
        if sum(case) > target:
            continue
        if target - sum(case) < sub:
            sub = target - sum(case)
            card = case
    
    print(sum(card))
    
if __name__ == '__main__':
    main()