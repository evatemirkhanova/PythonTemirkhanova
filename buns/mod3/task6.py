sentence = input().split()
print(*[s[-1] for s in sentence], sep = '')