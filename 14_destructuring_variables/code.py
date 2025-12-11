# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")
people = ("Bob", 42, "Mechanic")
name, _, profession = people
print(name, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)