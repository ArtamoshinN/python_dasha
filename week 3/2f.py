s = input()
pos1 = s.find('f')
if s.find('f', pos1 + 1) != -1:
    s = s[pos1 + 1:]
    pos2 = s.find('f')
    print(pos2 + pos1 + 1)
elif s.find('f', pos1 + 1) == -1 and pos1 != -1:
    print(-1)
elif pos1 == -1:
    print(-2)
