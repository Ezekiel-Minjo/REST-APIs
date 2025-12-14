def add(x, y):
    result = x + y
    print(result)

add(5, 3)

def say_hello(name, surname):
    print(f"hello, {name} {surname}")
say_hello(name="Ezekiel", surname="minjo")

def divide(dividend, divisor):
    if divisor !=0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(15, divisor=5)        