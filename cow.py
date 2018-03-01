n = int(input())
a = n % 10
b = n // 10
if a == 1 and b != 1:
    print(n, 'korova')
elif 2 <= a <= 4 and b != 1:
    print(n, 'korovy')
else:
    print(n, 'korov')
