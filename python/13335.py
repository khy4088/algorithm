import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())

trucks = list(map(int, input().split()))

time = 0

bridge = deque()
for _ in  range(w):
    bridge.append(0)
truck_num = 0

complete = []

while True:
    time += 1
    out = bridge.popleft()
    if out != 0:
        complete.append(out)
    else:
        pass
    
    if truck_num == len(trucks):
        bridge.append(0)
    elif len(bridge) < w and sum(bridge) + trucks[truck_num] <= L:
        bridge.append(trucks[truck_num])
        truck_num += 1
    else:
        bridge.append(0)
    
    if len(complete) == len(trucks):
        break
    
print(time)