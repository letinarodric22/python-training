
tasklist = [23, "Jane", (560), ["Lesson", "Maths", {"currency": "KES"}], 987, (76, "John")]

# 1. Print KES
task_list1 = tasklist[3][-1]
task_list1 = task_list1["currency"]
print(task_list1)

# 2. Print 560
task_list2 = (tasklist[2])
print(task_list2)

# 3. Print Maths
task_list3 = tasklist[3][-2]
print(task_list3)

# 4. In the dictionary with the key currency, add another key “amount” with value 90
task_list4 = tasklist[3][-1]
task_list4["amount"] = 90
task_list4 = tasklist
print(tasklist)

# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
# no = 987
# r_no = 0
# r_no = (r_no * 10) + (no % 10)
# no = no // 10
# r_no = (r_no * 10) + (no % 10)
# no = no // 10
# r_no = (r_no * 10) + (no % 10)
# print(r_no)

task_list5 = str(tasklist[-2])
task_list5 =task_list5[::-1]
tasklist[-2] = task_list5
print(tasklist)

# 6. Change the name “John” to “Jane” .
list(tasklist[-1])
tasklist[-1] = "Jane"
tasklist = (tuple(tasklist))
print(tasklist)
