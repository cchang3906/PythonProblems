ninth = []
tenth = []
eleventh = []
twelfth = []

flag9 = True 
flag10 = True
flag11 = True
flag12 = True

while True:
    name = input("Enter student's name, 0 to quit: ")
    if len(name)==0:
        print("Error: Empty input")
        continue
    if name.isnumeric():
        name = int(name)
    
    if name == 0:
        for student in ninth:
            if flag9 == True:
                print("9th graders in the dining hall are:")
                flag9 = False
            print(student)
        for student in tenth:
            if flag10 == True:
                print("10th graders in the dining hall are:")
                flag10 = False
            print(student)
        for student in eleventh:
            if flag11 == True:
                print("11th graders in the dining hall are:")
                flag11 = False
            print(student)
        for student in twelfth:
            if flag12 == True:
                print("12th graders in the dining hall are:")
                flag12 = False
            print(student)
        break
    grade = int(input("Enter student's grade: "))
    if int(grade) < 9 or int(grade) > 12:
        print("Error: Invalid Grade Input")
        continue
    
    if grade == 9:
        ninth.append(name);
    elif grade == 10:
        tenth.append(name);
    elif grade == 11:
        eleventh.append(name);
    else:
        twelfth.append(name);

