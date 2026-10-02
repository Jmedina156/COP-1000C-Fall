name = input("Enter name: ")

grade1 = int(input("Enter grade1: "))
grade2 = int(input("Enter grade2: "))
grade3 = int(input("Enter grade3: "))
grade4 = int(input("Enter grade4: "))
grade5 = int(input("Enter grade5: "))

classesGrades = [grade1, grade2, grade3, grade4, grade5]

gradesAverage = sum (classesGrades) / 5

def gradeLetter (gradeAverage) :
    if gradeAverage >= 90 :
        return "A"
    elif gradeAverage >= 80 :
        return "B"
    elif gradeAverage >= 70 :
        return "C"
    elif gradeAverage >= 60 :
        return "D"
    elif gradeAverage >= 50 :
        return "F"

finalLetter = gradeLetter(gradesAverage)

print("")

print (name)
print("Average: ", gradesAverage)
print("Letter grade: ", finalLetter)