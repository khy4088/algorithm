R = 31
M = 1234567891

def get_moded_power(n, p, M):
    t = 1
    for i in range(p):
        t *= n
        t %= M
    return t
     
L = int(input())

string = input()

result = 0
for idx in range(len(string)):
    # print(ord(char)-96)
    
    a_i = ord(string[idx]) - 96
    r_power_i = get_moded_power(R, idx, M)
    result += a_i * r_power_i 

print(result % 1234567891)