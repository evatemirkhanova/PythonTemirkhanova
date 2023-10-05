phone_number = input()
acceptable_symbols = '+0123456789'

result = ''
for i in range(len(phone_number)):
    if phone_number[i] in acceptable_symbols:
        result += phone_number[i]
print(result)