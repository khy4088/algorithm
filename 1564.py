def main():
    n = int(input())
    f = 1
    for i in range(2, n+1):
        f *= i
        
        while (f % 10 == 0) and (f>=100000):
            f /= 10
            f = int(f)
            
        f = int(f % 1e12)
        
        
    print("%05d" % (f % 100000))
        
if __name__ == '__main__':
    main()