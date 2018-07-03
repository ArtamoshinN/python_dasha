def power(a, n):
    if n == 0:
        return 1
    while n != 0 and n != 1:
        return a * a
        n -= 1
    return a
a = float(input())
n = int(input())
print(power(a, n))
