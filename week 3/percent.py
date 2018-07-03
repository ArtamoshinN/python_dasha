p = float(input())
x = int(input())
y = int(input())
s = int(x * 100 + y + (x * p) + (y * p / 100)) / 100
x = int(s)
y = int(s * 100 % 100)
print(x, y)
