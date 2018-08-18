loginAttempts = 3


def startUpMenu():
    print("""Press 1: Student login
Press 2: New user
Press 3: Teacher login
Press 4: Exit""")
    option = input(">>")
    if option == "1":
        studentlogin()
    elif option == "2":
        newUser()
    elif option == "3":
        teacherLogin()
    elif option == "4":
        exit()
    else:
        "Invalid details", startUpMenu()

def runQuiz(subjectDifficulty):
    print("Opening file",subjectDifficulty)
    score = 0
    quizOption = open(subjectDifficulty+".txt","r")
    for line in quizOption:
        line=line.strip("\n")
        ques,posAns,ansLoc=line.split(":")
        print(ques)
        posAns=posAns.split(",")
        qno = 1
        for eachAns in posAns:
            print("press",qno,"for",eachAns)
            qno+=1
        answer = input(">>")
        if answer == ansLoc:
            print("correct")
            score += 1
        else:
            print("incorrect")
    print(userName,"you scored",score)
    quizOption = open("Results.txt","a")
    quizOption.write(userName+":"+subjectDifficulty+":"+str(score)+"\n")
    quizOption.close()

def mainMenu():
    print("Welcome to the main menu")
    print("Math or comp")
    subject = input(">>>")
    while subject != "Math" and subject != "Comp":
        subject = input("Inavlid option, try again. \n>> ")
    print("Difficulty,/E for easy/M for medium/H for hard")
    diff = input(">>>")
    while diff != "H" and diff != "M" and diff != "E":
        diff = input("Invalid option, try again \n>>")
    fileName = subject+diff
    runQuiz(fileName)

def teacherArea():
    print("Welcome to the teachers area")


def teacherLogin():
    print("Welcome, teacher")
    tLog = "admin"
    tPw = "Password"
    teacher = input("Enter your name      : ")
    password = input("Enter your password : ")
    if tLog == teacher and tPw == password:
        return teacherArea()
    else:
        "Invalid details", startUpMenu()


def newUser():
    print("Welcome new user ")
    newUsers = open("Users.txt", "a")
    name = input("Enter your name     : ")
    surname = input("Enter your surname  : ")
    age = input("Enter your age      : ")
    password = input("Enter your password : ")
    userName = name[0:3] + age
    print(userName)
    newUsers.write(userName + ":" + password + ":" + name + ":" + surname + ":" + age + "\n")
    newUsers.close
    startUpMenu()


def studentlogin():
    global userName, loginAttempts
    userName = input("Enter Your username: ")
    password = input("Enter Your password: ")
    loginUser = open("Users.txt", "r")
    for eachline in loginUser:
        user, pW, name, surName, age = eachline.split(":")
        if user == userName and password == pW:
            print("welcome", name)
            mainMenu()
        else:
            print("Invalid details")
            loginAttempts = loginAttempts - 1
            print("Amount of attempts left,", loginAttempts)
            if loginAttempts > 0:
                studentlogin()
            elif loginAttempts == 0:
                print("You,ve run out of attemps, your now in the start up menu.")
                startUpMenu()


startUpMenu()
