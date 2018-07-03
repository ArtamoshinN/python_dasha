def digress(a, n):
    while n != 0:
        if n % 2 == 0:
            return digress(a**2, n / 2)
            break
        elif n % 2 != 0:
            return a * digress(a, n - 1)
    return a ** n
a = float(input())
n = int(input())
print(digress(a, n))
