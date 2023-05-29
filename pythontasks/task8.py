speed = int(input("Enter speed: "))
limit = 70
demerit_points = 0

if speed < limit:
    print("OK")
else:
    demerit_points = (speed - limit) // 5

    if demerit_points > 12:
        print("License suspended")
    else:
        print("Points: ", demerit_points)