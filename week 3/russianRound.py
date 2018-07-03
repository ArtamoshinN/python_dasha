x = float(input())
b = int(x)
x = x * 10 % 10
if x >= 5:
    print(b + 1)
else:
    print(b)
