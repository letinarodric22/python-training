# loop is used to get values from inside a data structure like a list
# or tuple
# if i want to repeat a task 10 times. i will store num 1 to num 10 in a list then
# loop through that list. In the body of the loop you can execute any other code
# like IF, indexing, slicing, accessing operations or  methods or even any other loop

# only display number divisible by 3
# list1 = list(range(0, 10))
# for i in list1:
#     if i % 3 == 0:
#         print(i)
    # i display the individual number that is from 0 to 9
# Display only cities that have letter a    
list2 = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"]
res = []
for i in list2:
    if "a" in i:
        res.append(i)
print(res)
        