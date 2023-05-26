
# # TASK2
# number = int(input("Enter the number: "))
# if number % 2 == 0:
#     print("this number is even")
# if number % 4 == 0:
#     print("and divisible by 4")
# else:
#     print("this number is odd")

# TASK3

# phone_number = str(input("enter the phone number: "))
# phone_number = phone_number.strip
# if phone_number[0:3] is "+254":
#     print(phone_number)
# elif phone_number[0:1] is "07" or "71" "01":
#     print(phone_number)

# phone_number = input("Enter a phone number: ")

# if phone_number.startswith("+254"):
#     print("Phone number is in correct format.")
# else:
#     if phone_number.startswith("07"):
#         phone_number = "+254" + phone_number[1:]
#     elif phone_number.startswith("71"):
#         phone_number = "+254" + phone_number[1:]
#     elif phone_number.startswith("254"):
#         phone_number = "+254" + phone_number[3:]
#     elif phone_number.startswith("01"):
#         phone_number = "+254" + phone_number[1:]
#     else:
#         print("Invalid phone number.")
#         exit()

#     print(phone_number)


# TASK 4
# email = str(input("enter the email: "))
# email.strip().lower()
# if "@" in  email[1:-2]:
#     print(email)
# else:
#     print("invalid email")

# # TASK 5
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))

# if num1 > num2 and num1 > num3:
#     print("num1 is the largest")
# elif num2 > num1 and num2 > num3:
#     print("num2 is the largest")
# else:
#     print("num3 is the largest")


# # TASK 6

# password = "admin@123"
# attempts = 4

# if attempts > 0:
#     user_password = input("Enter the password: ")

#     if user_password == password:
#         print("Access granted!")
#     else:
#         attempts -= 1
#         print("Incorrect password. Attempts left:", attempts)

#         if attempts > 0:
#             user_password = input("Enter the password: ")

#             if user_password == password:
#                 print("Access granted!")
#             else:
#                 attempts -= 1
#                 print("Incorrect password. Attempts left:", attempts)

#                 if attempts > 0:
#                     user_password = input("Enter the password: ")

#                     if user_password == password:
#                         print("Access granted!")
#                     else:
#                         attempts -= 1
#                         print("Incorrect password. Attempts left:", attempts)

#                         if attempts > 0:
#                             user_password = input("Enter the password: ")

#                             if user_password == password:
#                                 print("Access granted!")
#                             else:
#                                 attempts -= 1
#                                 print("Incorrect password. Attempts left:", attempts)
#                         else:
#                             print("Account blocked.")
#                 else:
#                     print("Account blocked.")
# else:
#     print("Account blocked.")


# # TASK 7
# marks = int(input("Enter marks: "))
# # marks = range(0,100)
# if marks >= 79:
#     print("A")
# elif marks < 79 and marks >= 60:
#     print("B")
# elif marks < 60 and marks >= 49:
#     print("C")
# elif marks < 49 and marks >= 40:
#     print("D")
# else:
#     print("E")


# # TASK 8

# speed = int(input("Enter speed: "))

# limit = 70
# demerit_points = 0

# if speed < limit:
#     print("OK")
# else:
#     demerit_points = (speed - limit) // 5

#     if demerit_points > 12:
#         print("License suspended")
#     else:
#         print("Points: ", demerit_points)


# TASK 9 IN STARS.PY

# # TASK 10
# prods = [['omo','30Kshs','300'],['milk','50Kshs','200'],['bread','45Kshs','359'],['coffee','5Kshs','79']]
# total = int(prods[0][2]) + int(prods[1][2]) + int(prods[2][2]) + int(prods[-1][-1])
# print(total)

# # TASK 11
# import datetime
# dob_input= (input("enter your date of birth (YYYY-MM-DD): "))
# dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
# today = datetime.date.today()
# age = today.year - dob.year
# if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
#     age -= 1
# dob_this_year = datetime.date(today.year, dob.month, dob.day)
# days_difference = (today - dob_this_year).days
# months = days_difference // 30
# days = days_difference % 30
# print(f"Age: {age} years, {months} months, {days} days")

# # TASK 12
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))

# if num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
#     print("The numbers entered should not be repeated.")
# else:
#     largest = max(num1, num2, num3, num4)
#     print("The largest number is:", largest)


# # TASK 13
# MAX_TRIES = 3
# email = "admin@mail.com"
# password = "Admin@123"
# tries = 0

# while tries < MAX_TRIES:
#     entered_email = input("Enter your email: ")
#     entered_password = input("Enter your password: ")

#     if entered_email == email and entered_password == password:
#         print("Login is Successful")
#         break
#     else:
#         tries += 1
#         print("Invalid username or password. Try again.")

# if tries == MAX_TRIES:
#     print("You have been blocked.")

# # TASK 14
# while True:
#     num1 = input("Enter the first number: ")
#     num2 = input("Enter the second number: ")
#     if num1.isdigit() and num2.isdigit():
#         result = int(num1) + int(num2)
#         print("Result: ", result)
#         break
#     else:
#         try:
#             num1 = float(num1)
#             num2 = float(num2)
#             result = num1 + num2
#             print("Result: ", result)
#             break
#         except ValueError:
#             print("Invalid character entered. Please enter numbers or floats only.")
#             continue

          

# rows = int(input("enter the number: "))

# if rows <= 0:
#     print("please enter a positive number")
# else:
#     for i in range(1, rows + 1):
#         print('*' * i)
   

salary = float(input("enter the basic salary: "))
benefit = float(input("Enter the benefits: "))
gross = salary + benefit
if gross <= 0:
    print('The amount is invalid. Please check again.')
elif gross > 0 and gross <= 5999:
    print(150)
elif gross >= 6000 and gross <= 7999:
    print(300)
elif gross >= 8000 and gross <= 11999:
    print(400)
elif gross >= 12000 and gross <= 14999:
    print(500)
elif gross >= 15000 and gross <= 19999:
    print(600)
elif gross >= 20000 and gross <= 24999:
    print(750)
elif gross >= 25000 and gross <= 29999:
    print(850)
elif gross >= 30000 and gross <= 34999:
    print(850)
elif gross >= 35000 and gross <= 39999:
    print(900)
elif gross >= 40000 and gross <= 44999:
   print(1000)
elif gross >= 45000 and gross <= 49999:
    print(1100)
elif gross >= 50000 and gross <= 59999:
    print(1200)
elif gross >= 60000 and gross <= 69999:
   print(1300)
elif gross >= 70000 and gross <= 79999:
   print(1400)
elif gross >= 80000 and gross <= 89999:
   print(1500)
elif gross >= 90000 and gross <= 99999:
    print(1600)
else:
    print(1700)