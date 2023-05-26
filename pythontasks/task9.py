row = int(input("Enter the number of rows: "))

if row <= 0:
    print("please enter positive number")
else:
    for i in range(1, row + 1):
        print("*" * i)