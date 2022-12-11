import sys
from itertools import permutations

def get_score(num: str, strike: int, ball: int, num_list: list) -> list:
    scores = []
    for i in num_list:
        temp_strike = 0
        temp_ball = 0
        for idx in [0,1,2]:
            if i[idx] == num[idx]:
                temp_strike += 1
            elif i[idx] in num:
                temp_ball += 1
        if temp_strike == strike and temp_ball == ball:
            scores.append(i)
    
    return scores


T = int(sys.stdin.readline())

result = [''.join(i) for i in permutations(['1','2','3','4','5','6','7','8','9'], 3)]

for _ in range(T):
    num, strike, ball = map(str, sys.stdin.readline().split())
    result = get_score(num, int(strike), int(ball), result)


print(len(result))