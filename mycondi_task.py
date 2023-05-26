# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))

# if num1 > num2 and num1 > num3:
#     print("num1 is the largest")
# elif num2 > num1 and num2 > num3:
#     print("num2 is the largest")
# else:
#     print("num3 is the largest")

number = int(input("Enter the number: "))
if 0 <= number <= 100:
    if number >= 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid")