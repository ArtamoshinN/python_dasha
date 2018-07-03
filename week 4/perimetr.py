def distance(x1, y1, x2, y2):
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return (x + y)**0.5

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
p = distance(x1, y1, x2, y2) + distance(x1, y1, x3, y3)
p += distance(x2, y2, x3, y3)
print(p)
