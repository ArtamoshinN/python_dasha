s = input()
pos1 = 0
while s.find('h', pos1) != -1:
    pos2 = s.find('h', pos1)
    pos1 = pos2 + 1
pos1 = s.find('h')
s1 = s[:pos1 + 1]
s2 = s[pos1 + 1:pos2]
s3 = s[pos2:]
print(s1 + s2 * 2 + s3)
