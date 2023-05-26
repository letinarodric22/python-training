num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

if num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
    print("The numbers entered should not be repeated.")
else:
    largest = max(num1, num2, num3, num4)
    print("The largest number is:", largest)