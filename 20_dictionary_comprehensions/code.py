users = [
    (0, "Bob", "Password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])

username_input = input("Enter your username: ")
username_password = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if username_password == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")    