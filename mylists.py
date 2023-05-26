person = ["John Doe", 30, "john@mail.com", "Nairobi"]
person1 = person[2]
print(person1)


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[0:])
day_today = days[1]
print(day_today)
print(len(days))

total = str(person) + str(days)
print(total)


mylists = days + days 
print(mylists)
print(len(mylists))

mylists1 = days * 4
print(mylists1)
print(len(mylists1))


days_3 = days[2:5]
print(days_3)

days_4 = days in ["Wednesday"]
days_4 = bool(days)
print(days_4)




# del days[0]
# print(days)

# updating
days[3] = "thur"
print(days)
# appending - adding a value to the end of a list
days.extend(["NAIROBI","kenya","NGONG"])
print(days)





trainees = ["john",[2,["James", "Mary"]]]

# Display 2 using index, from the list.
trainees1 = trainees[1][0]
print(trainees1)

# Output James  using index, from the list.
trainees2 = trainees[1][1][0]
print(trainees2)

# Using a method add 56 at the end of the list.=
trainees.append(56)
print(trainees)

# Using a method add the name Mike between James and Mary
trainees[1][1].insert(1, "Mike")
print(trainees)

# Change the value of 2 to 8
trainees[1][0] = 8
print(trainees)

# Remove John and Mary from the list.
del trainees[0] 
trainees3 = trainees[-2]
trainees4 = trainees3[1]
del trainees4[2]
trainees4 = trainees
print(trainees)
# del trainees[0][1][-1]
# print(trainees)

#  Using a function, determine the length of the list
print(len(trainees))








