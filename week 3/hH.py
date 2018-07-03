s = input()
h1 = s.find('h')
h2 = s.rfind('h')
sub = s[h1 + 1:h2]
sub = sub.replace('h', 'H')
print(s[:h1 + 1] + sub + s[h2:])
