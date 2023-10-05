s = input()
i = input()

i_count = 0
        
if s[0] == i:
    for c in range(len(s)):
        if s[c] == i:
            i_count += 1
            continue
        else:
            break
print(i_count)