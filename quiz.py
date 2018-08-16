def startUpMenu():
    print("""Press 1: Student login
Press 2: New user
Press 3: Teacher login
press 4: new teacher
Press 5: Exit""")
    option=input(">>")
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


def mainMenu():
    print("Welcome to the main menu")

def teacherArea():
    print("Welcome to the teachers area")

def teacherLogin():
    print("Welcome, teacher")
    tLog="admin"
    tPw ="Password"
    teacher=input("Enter your name      : ")
    password=input("Enter your password : ")
    if tLog==teacher and tPw==password:
        return teacherArea()
    else:
        "Invalid details", startUpMenu()

def newUser():
    print("Welcome new user ")
    file     = open("Users.txt","a")
    name     = input("Enter your name     : ")
    surname  = input("Enter your surname  : ")
    age      = input("Enter your age      : ")
    password = input("Enter your password : ")
    userName = name[0:3] + age
    file.write(userName+":"+password+":"+name+":"+surname+":"+age+"\n")
    file.close
    startUpMenu()

def studentlogin():
    countOFLoginAttempts = 3
    global loginUserName
    loginUserName = input("Enter Your username: ")
    password = input("Enter Your password: ")
    file = open("Users.txt","r")
    for eachline in file:
        user,pW,name,surName,age=eachline.split(":")
        if user==loginUserName and password==pW:
            print("welcome",name)s
            mainMenu()
        else:
            print("Invalid details")
            countOFLoginAttempts = countOFLoginAttempts - 1
            print("Amount of attempts left,",countOFLoginAttempts)
            studentlogin()
            if countOFLoginAttempts == -1:
                print("You,ve run out of attemps, your now in the start up menu.")
                startUpMenu()



startUpMenu()
