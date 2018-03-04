a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    (a, c) = (c, a)
    if a > b:
        (a, b) = (b, a)
        print(a, b, c)
    else:
        print(a, b, c)
elif b >= a and b >= c:
    (b, c) = (c, b)
    if a > b:
        (a, b) = (b, a)
        print(a, b, c)
    else:
        print(a, b, c)
elif c >= a and c >= b:
    if a > b:
        (a, b) = (b, a)
        print(a, b, c)
    else:
        print(a, b, c)
else:
    print(a, b, c)
