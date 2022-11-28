import sys

T = int(input())

pattern_L, pattern_R = map(str, sys.stdin.readline().rstrip().split('*'))


for _ in range(T):
    test = sys.stdin.readline().rstrip()
    if test[0:len(pattern_L)] == pattern_L and test[len(pattern_L):][-len(pattern_R):] == pattern_R:
        print('DA')
    else:
        print('NE')

