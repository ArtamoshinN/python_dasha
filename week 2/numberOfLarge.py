n1 = int(input())
i = 0
while n1 != 0:
    n2 = int(input())
    if n2 > n1:
        i += 1
    n1 = n2
print(i)
