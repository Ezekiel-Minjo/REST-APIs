numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print (doubled)
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = [s for s in friends if s.startswith("S")]

# for s in friends:
#     if s.startswith("S"):
#         start_s.append(s)

print(start_s)