fin = open('input.txt', 'r', encoding='utf8')
b = []
for i in fin:
    a = i.split()
    b += a
b = set(b)
print(len(b))
