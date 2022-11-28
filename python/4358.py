import sys


tree_dic = {}
count = 0

while True:
    name = sys.stdin.readline().rstrip()
    if name == '':
        break
    
    if name in tree_dic:
        tree_dic[name] += 1
        count += 1
    else:
        tree_dic[name] = 1
        count += 1
        
        
for name in sorted(tree_dic.keys()):
    print('{:s} {:.4f}'.format(name, tree_dic[name] * 100 / count))

