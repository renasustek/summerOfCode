####VARIABLES####
loginAttempts = 3


####VARIABLES####

####MENUS####
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
        print("Invalid option")
        startUpMenu()


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
    fileName = subject + diff
    runQuiz(fileName)


def teacherArea():
    print("Welcome to the teachers area")
    print("""Press 1: Search for a student
Press 2: Search by topic
Press 3: Start menu
Press 4: exit""")
    searchOption = input(">>")
    if searchOption == "1":
        findstudent()
    elif searchOption == "2":
        findTopic()
    elif searchOption == "3":
        startUpMenu()
    elif searchOption == "4":
        exit()
    else:
        print("Invalid option,try again")
        teacherArea()


####MENUS####

####NEW USERS####
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


####NEW USERS####

####LOGIN####
def studentlogin():
    global userName, loginAttempts
    userName = input("Enter Your username: ")
    password = input("Enter Your password: ")
    loginUser = open("Users.txt", "r")
    for eachline in loginUser:
        user, pW, name, surName, age = eachline.split(":")
        if user == userName and password == pW:
            print("welcome", name)
            return mainMenu()
        else:
            print("Invalid details")
            loginAttempts = loginAttempts - 1
            print("Amount of attempts left,", loginAttempts)
            if loginAttempts > 0:
                studentlogin()
            elif loginAttempts == 0:
                print("You,ve run out of attemps, your now in the start up menu.")
                startUpMenu()


def teacherLogin():
    print("Welcome, teacher")
    tLog = "admin"
    tPw = "password"
    teacher = input("Enter your name      : ")
    password = input("Enter your password  : ")
    if tLog == teacher and tPw == password:
        teacherArea()
    else:
        print("Invalid details")
        startUpMenu()


####LOGIN####

####QUIZ####
def runQuiz(subjectDifficulty):
    print("Opening file", subjectDifficulty)
    score = 0
    quizOption = open(subjectDifficulty + ".txt", "r")
    for line in quizOption:
        line = line.strip("\n")
        ques, posAns, ansLoc = line.split(":")
        print(ques)
        posAns = posAns.split(",")
        qno = 1
        for eachAns in posAns:
            print("press", qno, "for", eachAns)
            qno += 1
        answer = input(">>")
        if answer == ansLoc:
            print("correct")
            score += 1
        else:
            print("incorrect")
    print(userName, "you scored", score)
    quizOption = open("Results.txt", "a")
    quizOption.write(userName + ":" + subjectDifficulty + ":" + str(score) + "\n")
    quizOption.close()


####QUIZ####

####TEACHER RECORCES####
def findstudent():
    someOneFound = False
    print("Enter student's username")
    lookingFor = input(">>")
    findingResult = open("Results.txt", "r")
    for line in findingResult:
        userName, testName, score = line.split(":")
        if userName == lookingFor:
            print("For", testName, userName, "Scored: ", score)
            someOneFound = True
    if someOneFound == False:
        print("sorry,", lookingFor, "has not done any quizes.")
    teacherArea()


def findTopic():
    print("What topic are you looking for")
    averageScoreList = []
    highScore = 0
    highScoreNameList = []
    print("PLease select a subject between Math or Comp")
    subject = input(">>")
    while subject != "Math" and subject != "Comp":
        subject = input("invalid option, try again \n>>")
    print("Select difficulty E M H")
    difficulty = input(">>")
    while difficulty != "H" and difficulty != "M" and difficulty != "E":
        difficulty = input("invalid option,try again\n>>")
    fileName = subject + difficulty
    file = open("results.txt", "r")
    for line in file:
        userName, testName, score = line.split(":")
        score = int(score)
        if testName == fileName:
            averageScoreList.append(score)
            if score > highScore:
                highScore = score
                highScoreNameList = [userName]
            elif score == highScore:
                if userName not in highScoreNameList:
                    highScoreNameList.append(userName)
            else:
                pass
    if len(highScoreNameList) != 0:
        print("for test", fileName)
        print("the highest score was", highScoreNameList)
        print("achived by", highScoreNameList)
        aveScore = sum(averageScoreList) / len(averageScoreList)
        print("the average score for this test is", aveScore)
    else:
        print("no one, no one has completed this test")
        teacherArea()


####TEACHER RECORCES####


####FUNCTIONS####
startUpMenu()
####FUNCTIONS####
