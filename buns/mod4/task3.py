def gcd(a, b):
    if a == 0 and b != 0:
        return b - a
    elif a != 0 and b == 0:
        return a - b
    elif a > b:
        return gcd(a%b, b)
    else:
        return gcd(a, b%a)

a = int(input())
b = int(input())
print(gcd(a, b))