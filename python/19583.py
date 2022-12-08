import sys

def get_time(time:str) -> int:
    h, m = map(int, time.split(':'))
    return h * 60 + m

S, E, Q = map(get_time, sys.stdin.readline().rstrip().split())
# print(S,E,Q)
attend = {}
start = {}
end = {}
count = 0

while True:
    chat = sys.stdin.readline().rstrip()
    if chat == '':
        break
    time, name = map(str, chat.split())
    time = get_time(time)
    if time <= S:
        start[name] = ''
    elif E <= time <= Q:
        end[name] = ''
    
for name in start:
    if name in end:
        count += 1 
        
print(count)
    