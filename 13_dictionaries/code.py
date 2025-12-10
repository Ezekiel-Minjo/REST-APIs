friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Adam"])

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]
print(friends[1]["name"])


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}


for student, attendance in student_attendance.items():
    print(f"{student}: {attendance} ")

my_dictionary = {'a': 1, 'b': 2, 'c': 3}
items = list(my_dictionary.items())
print(items)    