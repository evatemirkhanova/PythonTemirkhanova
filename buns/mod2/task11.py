string = input()
was_in_string = ''

result = False
for i in range(len(string)):
    if (string[i] != ' ') and (string[i] in was_in_string):
        result = True
        break
    was_in_string += string[i]
        
print(result)