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