import math
x = 34

y = 7
z = x**y
print(z)

print(y%x)



print(x//y)
# task1
temp = 56.8926
temp1 = math.ceil(temp)
print(temp1)


temp2 = math.floor(temp)
print(temp2)

# task 2

temp3 = round(temp, 2)
print(temp3)

# task 3
temp4 = round(temp, 3)
print(temp4)


# task 4
temp5 = round(temp % 10, 3)
print(temp5)


temp = str(temp)
temp = temp[3:]
temp = temp[0:1] + "." + temp[1:]
temp = float(temp)
print(temp)

# area=math.pi * 7 * 7
# print(area)

# print(area * 2)


# print(area//1)
# print(area%2)



# # write a python program to calculate the length of the strings
# mysent = "kenya is the richest country in africa"
# mysent1 = "programming is the best skill to have in this world "
# mypara = mysent + mysent1
# print(len(mypara))


# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#             return dict
#         print(char_frequency("google.com"))



num = input("enter a value: ")
print(num)
# prompt the user for 2 number  