def power_to(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_to(a**2, n/2)
    else:
        return a * power_to(a, n-1)

a = int(input())
n = int(input())
print(power_to(a, n))
