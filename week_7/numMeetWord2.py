fin = open('input.txt', 'r', encoding='utf8')
count = {}
words = list()
for line in fin:
    words += list(line.strip().split())
for i in words:
    count[i] = count.get(i, 0) + 1
    print(count[i] - 1, end=' ')
