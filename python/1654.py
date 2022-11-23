import sys

def binary_search(num_list, target_count):
    start = 1
    end = max(num_list)

    while start <= end:
        mid = (start + end) // 2
        count = sum([i // mid for i in num_list])
        if count >= target_count:
            start = mid + 1
        elif count < target_count:
            end = mid - 1
        

    return end


K, N = map(int, sys.stdin.readline().rstrip().split())

lan = []

for _ in range(K):
    lan.append(int(input()))

print(binary_search(lan, N))