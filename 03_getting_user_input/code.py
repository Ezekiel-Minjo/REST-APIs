size_input = int(input("How big is your house (in square feet): "))
# square_feet = int(size_input)
square_metres = size_input / 10.8
print(square_metres)
print(f"{size_input} square feet is {square_metres:.2f} square metres")