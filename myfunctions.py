# # functions perform a specific task in your program and they are meant to organize your code.
# # reusable
# # 1. take in data
# # 2. process the data
# # 3. return a value

# # instagram app functions
# # 1. login
# # data - username, password
# # task - clean up the data then check if they match the ones in a database.  
# # info - data type of output is: boolean(True or False)

# # 2. messaging()
# # 3. update()

# # come up with all possible functions in ig app, describe data take in, task it does and value it return


# # def greet(f_name, l_name):
# #     print(f"hi {f_name} {l_name}")
# #     print("feel at home")


# # greet("nairobi", "kenya")  




# # def calculate(x, y):
# #     t = x - y
# #     return t

# # t1=calculate(30, 60)
# # print(t1)

# # t2 = calculate(20, 10)
# # print(t2)


# # parameters and arguements in fuctions
# # the below in brackets(paranthesis) are parameters.
# # variables are only visible inside a function.
# def t_marks(maths,eng,swa,sci,sos):
#     marks=maths+eng+swa+sci+sos
#     return marks

# def avg_marks(marks):
#        avg = marks / 5
#        return avg

# def find_grades(avg):
#     if avg > 79 and avg <= 100:
#         return "A"
#     elif avg >= 60 and avg <= 79:
#         return "B"
#     elif avg >= 59 and avg <= 49:
#         return "C"
#     elif avg >= 40 and avg <= 49:
#         return "D"
#     elif avg >= 0 and avg <= 40:
#         return "E"
#     else:
#         return "invalid average"
    
# maths=int(input("Enter maths's marks: "))
# eng=int(input("Enter eng marks: "))
# swa=int(input("Enter swa marks: "))
# sci= int(input("Enter sci marks: "))
# sos= int(input("Enter sos marks: "))

# total_marks=t_marks(maths,eng,swa,sci,sos)
# print(total_marks)

# avg=avg_marks(total_marks)
# print(avg)
    
# t3=find_grades(avg)
# print(t3)


     
# i = 1
# while i <= 10:
#     print("*" * i)
#     i=i+1

# def is_leap(year):
#     leap = False

#     if (year % 400 == 0) and (year % 100 == 0):
#         # return True
#         print(True)

#     elif (year % 4 ==0) and (year % 100 != 0):
#         # return True
#         print(True)

#     else:
#         # return False
#         print(False)
    
# is_leap(2016)



def calculator(x,y):
    z= x+y
    return z

lst = [23,56,8]









