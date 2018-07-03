n = float(input())
i = 2
s = 1
while i <= n:
    s += 1 / i**2
    i += 1
print('{0:.6f}'.format(s))
