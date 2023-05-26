MAX_TRIES = 3
email = "admin@mail.com"
password = "Admin@123"
tries = 0

while tries < MAX_TRIES:
    entered_email = input("Enter your email: ")
    entered_password = input("Enter your password: ")

    if entered_email == email and entered_password == password:
        print("Login is Successful")
        break
    else:
        tries += 1
        print("Invalid username or password. Try again.")

if tries == MAX_TRIES:
    print("You have been blocked.")