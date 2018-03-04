n = int(input())
i = 1
while i <= n:
    if n % i == 0 and i != 1:
        print(i)
        break
    else:
        i = i + 1
