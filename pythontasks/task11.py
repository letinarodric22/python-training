import datetime
dob_input= (input("enter your date of birth (YYYY-MM-DD): "))
dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
today = datetime.date.today()
age = today.year - dob.year
if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
    age -= 1
dob_this_year = datetime.date(today.year, dob.month, dob.day)
days_difference = (today - dob_this_year).days
months = days_difference // 30
days = days_difference % 30
print(f"Age: {age} years, {months} months, {days} days")