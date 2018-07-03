n = int(input())
h = ['HELP']
a = 0
mSet = set(range(1, n + 1))
while a != h:
    a = input().split()
    if a == h:
        break
    s = input()
    a = set(map(int, a))
    if s == 'YES':
        mSet &= a
    else:
        mSet -= a
print(*sorted(list(mSet)))
