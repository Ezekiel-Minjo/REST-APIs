friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}
local = {'Rolf'}
local_friends = friends.difference(abroad)
# print(local_friends)
friend = local.union(abroad)
# print(friend)

art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

pure_art = art.difference(science)
print(pure_art)
pure_science = science.difference(art)
print(pure_science)
students = art.union(science)
print(students)
both = art.intersection(science)
print(both)
