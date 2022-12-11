var = input()
string = ''
mode_java = False
mode_cplusplus = False
skip = False
error = False

if var[0] == '_' or var[-1] == '_':
    print('Error!')

elif 65 <= ord(var[0]) <= 90:
    print('Error!')

elif '__' in var:
    print('Error!')
    
else:
    for i in range(len(var)):
        if skip and 65 <= ord(var[i]) <= 90:
            error = True
            print('Error!')
            continue
        elif skip:
            skip = False
            continue
        if 65 <= ord(var[i]) <= 90:
            mode_java = True
            string +=  '_' + var[i].lower()
        elif var[i] == '_':
            mode_cplusplus = True
            string += var[i+1].upper()
            skip = True
        else:
            string += var[i]
        if mode_java and mode_cplusplus:
            print('Error!')
            error = True
            break
        
    if not error:
        print(string)