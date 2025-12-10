l = ['Bob', 'rolf', 'Anne']
t = ('Bob', 'rolf', 'Anne')
s = {'Bob', 'rolf', 'Anne'}

print(l[0], t[2], s)
l.append('smith')
print(l[3])
l.remove('Bob')
print(l)
s.add('smith')
s.add('smith')
print(s)