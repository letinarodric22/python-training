email = str(input("enter the email: "))
email.strip().lower()
if "@" in  email[1:-2]:
    print(email)
else:
    print("invalid email")

# TASK 5
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

if num1 > num2 and num1 > num3:
    print("num1 is the largest")
elif num2 > num1 and num2 > num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")