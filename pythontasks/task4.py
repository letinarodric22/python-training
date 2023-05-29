email = str(input("enter the email: "))
email.strip().lower()
if "@" and "." in  email[1:]:
    print("valid email", email)
else:
    print("invalid email")

