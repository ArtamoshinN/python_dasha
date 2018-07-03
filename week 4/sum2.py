def sum(s):
    n = int(input())
    if n != 0:
        s += n
    else:
        return s
    return sum(s)
s = 0
print(sum(s))
