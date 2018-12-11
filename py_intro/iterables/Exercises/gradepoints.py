grades = {'English':None,
          'Math':None,
          'Global Studies':None,
          'Art':None,
          'Music':None}


def main():
    global grades
    keyList = list(grades.keys())
    sumGrades = 0
    outputString = ""
    for key in keyList:
        prompt = "Enter " + key + " Grade: "
        thisGrade = int(input(prompt))
        outputString += key + " grade: " + str(thisGrade) + "\n"
        grades[key] = thisGrade
        sumGrades += thisGrade
        
    avgGrade = sumGrades/len(keyList)
    print("\n\n" + outputString)
    print("Your average is ",avgGrade)
    
    
    changeSubject = input("Enter Subject to Change: ")
    newGrade = int(input("Enter New " + changeSubject + " Grade: "))
    oldGrade = grades[changeSubject]
    avgGradeNew = (len(keyList)*avgGrade - oldGrade + newGrade)/len(keyList)
    grades[changeSubject] = newGrade
    print("Your new average is ",avgGradeNew)

main()