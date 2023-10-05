sentence = input()
result = ''

for i in range(len(sentence)):
    if sentence[i] == ' ':
        result += sentence[i-1]
        
result += sentence[-1]
print(result)