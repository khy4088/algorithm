import sys

def main():
    n = int(sys.stdin.readline().strip())
    nums = []
    for _ in range(n):
        nums.append(int(sys.stdin.readline().strip()))
        
    for i in sorted(nums):
        print(i)
        
if __name__ == '__main__':
    main()