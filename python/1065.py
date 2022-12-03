def solution(n):
    count = 0
    for i in range(1, n+1):
        if i < 100:
            count += 1
        elif i == 1000:
            i_0, i_1, i_2, i_3 = map(int, str(i))
            if i_0 - i_1 == i_1 - i_2:
                count += 1
        else:
            i_0, i_1, i_2 = map(int, str(i))
            if i_0 - i_1 == i_1 - i_2:
                count += 1
    return count


print(solution(int(input())))