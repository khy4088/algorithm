import sys

work_list = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
cnt = 0
while True:
    work = sys.stdin.readline().rstrip().split()
    if work == []:
        break
    for w in work:
        if w in ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']:
            work_list[w] += 1
    cnt += len(work)
    
for key in work_list.keys():
    print('%s %d %.2f' % (key, work_list[key], work_list[key]/cnt))
    
print('Total %d 1.00' % cnt)