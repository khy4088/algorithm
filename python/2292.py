def main():
    N = int(input())
    layer = 1
    last_num = 1
    while N > last_num:
        last_num = last_num + layer * 6
        layer += 1
            
    print(layer)
    
if __name__ == '__main__':
    main()
    