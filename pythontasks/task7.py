marks = int(input("Enter marks: "))
if marks >= 79 and marks <= 100:
    print("A")
elif marks < 79 and marks >= 60:
    print("B")
elif marks < 60 and marks >= 49:
    print("C")
elif marks < 49 and marks >= 40:
    print("D")
elif marks < 40 and marks >= 0:
    print("E")
else:
    print("invalid marks entered")