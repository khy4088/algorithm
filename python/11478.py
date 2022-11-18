import sys

string = input()
result = {}
count = 0
for i in range(len(string)):
    for j in range(i, len(string)+1):
        if i == j:
            pass
        else:
            if string[i:j] not in result:
                result[string[i:j]] = None

print(len(result))

