import sys

def main():
    sudoku = []
    sudoku_t = [[] for _ in range(9)]
    for _ in range(9):
        line = list(map(int, sys.stdin.readline().split()))
        sudoku.append(line)
        for i in range(9):
            sudoku_t[i].append(line[i])
        
    for line in sudoku:
        if line.count(0) >= 2:
            pass
        else:
            line[line.index(0)] = [x for x in [1,2,3,4,5,6,7,8,9] if x not in line][0]
    
    for line in sudoku:
        print(line)
        
if __name__ == '__main__':
    main()