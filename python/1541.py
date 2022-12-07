import sys

expression = sys.stdin.readline().rstrip().split('-')

num = 0
for plus in expression[0].split('+'):
    num += int(plus)

for exp in expression[1:]:
    for minus in exp.split('+'):
        num -= int(minus)
        
print(num)