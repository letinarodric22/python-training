password = "admin@123"
attempts = 4

if attempts > 0:
    user_password = input("Enter the password: ")

    if user_password == password:
        print("Access granted!")
    else:
        attempts -= 1
        print("Incorrect password. Attempts left:", attempts)

        if attempts > 0:
            user_password = input("Enter the password: ")

            if user_password == password:
                print("Access granted!")
            else:
                attempts -= 1
                print("Incorrect password. Attempts left:", attempts)

                if attempts > 0:
                    user_password = input("Enter the password: ")

                    if user_password == password:
                        print("Access granted!")
                    else:
                        attempts -= 1
                        print("Incorrect password. Attempts left:", attempts)

                        if attempts > 0:
                            user_password = input("Enter the password: ")

                            if user_password == password:
                                print("Access granted!")
                            else:
                                attempts -= 1
                                print("Incorrect password. Attempts left:", attempts)
                        else:
                            print("Account blocked.")
                else:
                    print("Account blocked.")
else:
    print("Account blocked.")