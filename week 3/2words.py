s = input()
pos = s.find(' ')
s1 = s[:pos]
s2 = s[pos + 1:]
space = ' '
print(s2 + space + s1)
