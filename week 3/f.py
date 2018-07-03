s = input()
pos = s.find('f')
if s.find('f', pos + 1) != -1:
    print(s.find('f'), end=' ')
    s = s[::-1]
    pos2 = s.find('f')
    print(len(s) - pos2 - 1)
elif s.find('f') != -1:
    print(s.find('f'))
