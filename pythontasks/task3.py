phone_number = str(input("enter the phone number: "))
phone_number = phone_number.strip
if phone_number[0:3] is "+254":
    print(phone_number)
elif phone_number[0:1] is "07" or "71" "01":
    print(phone_number)

phone_number = input("Enter a phone number: ")

if phone_number.startswith("+254"):
    print("Phone number is in correct format.")
else:
    if phone_number.startswith("07"):
        phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("71"):
        phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("254"):
        phone_number = "+254" + phone_number[3:]
    elif phone_number.startswith("01"):
        phone_number = "+254" + phone_number[1:]
    else:
        print("Invalid phone number.")
        exit()

    print(phone_number)