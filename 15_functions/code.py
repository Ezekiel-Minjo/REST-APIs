def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in seconds program!")
# user_age_in_seconds()

print("Goodbye")

friends = []
def add_friend(*names):
    for name in names:
        friends.append(name)

add_friend("zeki", "minjo", "fili")

print(friends) #[Rolf]