n = int(input())
i = 0
l = 1
m = n
while m != 0:
    m = m // 10
    i += 1
print(n % 10, end='')
while l < i:
    m = n
    m = (m // (10 ** l)) % 10
    print(m, end='')
    l += 1
