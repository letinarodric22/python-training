# functions perform a specific task in your program and they are meant to organize your code.
# reusable
# 1. take in data
# 2. process the data
# 3. return a value

# instagram app functions
# 1. login
# data - username, password
# task - clean up the data then check if they match the ones in a database.  
# info - data type of output is: boolean(True or False)

# 2. messaging()
# 3. update()

# come up with all possible functions in ig app, describe data take in, task it does and value it return


# def greet(f_name, l_name):
#     print(f"hi {f_name} {l_name}")
#     print("feel at home")


# greet("nairobi", "kenya")  




# def calculate(x, y):
#     t = x - y
#     return t

# t1=calculate(30, 60)
# print(t1)

# t2 = calculate(20, 10)
# print(t2)


# parameters and arguements in fuctions
def t_marks(m,e,k,sc,ss):
    total=m+e+k+sc+ss
    return total
# the above in brackets(paranthesis) are parameters.

marks= t_marks(67,53,46,77,60)
print(marks)
# the above in brackets(paranthesis) are arguements.
# marks=303 is setting a default value
def avg_marks(marks=303):
    avg = marks / 5
    return avg

t2=avg_marks()
print(t2)











