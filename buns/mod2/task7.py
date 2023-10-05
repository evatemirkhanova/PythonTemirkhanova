binary_str = input()
    
zero_count, unit_count = 0, 0

for i in range(len(binary_str)):
    if binary_str[i] == '0':
        zero_count += 1
    else:
        unit_count += 1 
if zero_count == unit_count:
    print('yes')
else:
    print('no')