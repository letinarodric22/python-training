
#strings are alphanumeric characters. alphabets, numbers and characters . UTF8
#Certain operations are done on strings ONLY
#1.converting casing   to lowercase or to uppercase
#2.splitting values
#3.count the number of times a word appears
#..etc
#To access these operations or methods we use a . after the variable name.
first_name = "John"
first_name = first_name.lower()
first_name.lower()
print(first_name)
 
last_name="  doe "
last_name = last_name.strip()
print(last_name)


email="     Mail2@Mail.com"
email = email.strip().lower()
print(email)
mail = "      leTINAroderick@gmail.com    "
mail = mail.lower().strip()
print(mail)
a = "sandaiya, letina roderick"
print(a[0])
# mydata ="(omo|ks4/ajdh/-96>letina)"
# print(email.count("@"))
print(email.count("m"))

mypara = "The days hash started well. I woke up at 5. My schedule is packed"

mysent = mypara.split(".")

print(mysent)
print(mypara.count("s"))
print(type(mysent))




# indexing is accessing a character in a variable by counting starting from 0
myname = "John Doe"
# print(myname[-2])

# Slicing- is when you want to access multiple characters in a variable.
# first part is using the index of where to start
# second part is the count of where to stop 
print(myname[0:4])


# display Doe using slicing. try with both negative and positive numbers

print(myname[5:8])
print(myname[-3:])

# length it find the length of characters
print(len(myname))
# print(myname[0:])
print(myname[-3:])




