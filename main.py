marks = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
gpas = [4.0, 3.7, 3.33, 3.0, 2.7, 2.33, 2.0, 1.7, 1.33, 1, 0.67, 0]
grades = []

def total():
    x = 0
    for i in grades:
        x = x + i
    print("Average GPA: %0.2f" % (x / len(grades)))
    quit()

def main():
    global grades
    for i in range(100): 
        while True:
            x = input("Enter a grade: ")
            if x in marks:
                for i in range(len(marks)):
                    if marks[i] == x:
                        grades.append(gpas[i])
            elif x.lower() in ["q", "quit"]:
                total()
            else:
                print("Invalid input")
                break

if __name__ == "__main__":
    main()
