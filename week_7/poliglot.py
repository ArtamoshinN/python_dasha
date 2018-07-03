n = int(input())
a = set()
b = set()
c = set()
if n != 0:
    num = int(input())
    if num != 0:
        for i in range(num):
            lang = input()
            a.add(lang)
            b.add(lang)
    if n - 1 != 0:
        for i in range(n - 1):
            num = int(input())
            if num != 0:
                for j in range(num):
                    lang = input()
                    a.add(lang)
                    c.add(lang)
            else:
                continue
            b &= c
            c = set()
print(len(b))
for i in b:
    print(i)
print(len(a))
for i in a:
    print(i)
