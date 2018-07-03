s = input()
pos1 = s.find('h')
if s.find('h', pos1 + 1) != -1:
    s = s[::-1]
    pos2 = s.find('h')
s = s[::-1]
print(s[:pos1], end='')
print(s[(len(s) - pos2):])
