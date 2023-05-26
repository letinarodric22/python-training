day = ("Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Sarturday", "Sunday")

# use an index to get wednesday
day3 = day[2]
print(day3)

# Slice to get Wednesday to Friday
Three_days = day[-6:-3]
print(Three_days)
# it is not possible to change a value that is in a tuple
day = list(day)
day[5] = "Satur"
day = tuple(day)
print(day)