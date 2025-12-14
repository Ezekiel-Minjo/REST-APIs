# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0.")
    
#     return dividend / divisor

# def calculate(*values, operator):
#     return operator(*values)
# try:
#     result = calculate(20, 0, operator=divide) 
#     print(result)  # Output: 5.0
# except ZeroDivisionError as e:
#     print(e)  # Output: Divisor cannot be 0.
from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise  RuntimeError(f"Could not find an element with {expected!r}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
    ]


try:
    print(search(friends, "Bob Smith", itemgetter("name")))  # Raises RuntimeError
except RuntimeError as e:
    print(e)  # Output: Could not find an element with 'Bob Smith'.    
