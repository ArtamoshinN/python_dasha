fin = open('input.txt', 'r', encoding='utf8')
c = list()
b = list()
count = 0
for i in fin:
    a = i.split()
    b += a
for j in range(len(b)):
    if b[j] in c:
        count = c.count(b[j])
        print(count, end=' ')
        count = 0
    else:
        print(count, end=' ')
    c.append(b[j])
