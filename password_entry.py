
MIN_LENGTH = 3

password = input("Enter password")

while len(password) < MIN_LENGTH:
    print("Password must be at least", MIN_LENGTH, " characters long")
    password = input("Enter password")

for i in password:
    print("*", end="")





