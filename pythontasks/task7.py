marks = int(input("Enter marks: "))
# marks = range(0,100)
if marks >= 79:
    print("A")
elif marks < 79 and marks >= 60:
    print("B")
elif marks < 60 and marks >= 49:
    print("C")
elif marks < 49 and marks >= 40:
    print("D")
else:
    print("E")