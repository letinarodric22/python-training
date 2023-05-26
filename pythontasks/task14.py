while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if num1.isdigit() and num2.isdigit():
        result = int(num1) + int(num2)
        print("Result: ", result)
        break
    else:
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 + num2
            print("Result: ", result)
            break
        except ValueError:
            print("Invalid character entered. Please enter numbers or floats only.")
            continue

        
rows = int(input("enter the number: "))

if rows <= 0:
    print("please enter a positive number")
else:
    for i in range(1, rows + 1):
        print('*' * i)