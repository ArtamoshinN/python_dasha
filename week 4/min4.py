def min4(a, b, c, d):
    m = min(min(a, b), min(c, d))
    return m
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
