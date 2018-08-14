def startUpMenu():
    print("Welcome to the quiz program")
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
        print("Invalid option")
        startUpMenu()
def defExitOption():
    extOption = input("Would you like to exit:(y/n)")
    if exitOption == "y":
        return startUpMenu()
    elif exitOption == "n":
        return login()
    else:
        return defExitOption()

def mainMenu():
    pass

def teacherLogin:
    print("Welcome, teacher")
    tLog="admin"
    tPw ="Password"
    teacher=input("Enter your name: ")
    password=input("Enter your password: ")
    if tLog==teacher and pW==password:
        return teacherArea()
    else:("Invalid details")
        defExitOption()



def newUser():
    print("Welcome new user ")
    file     = open("Users.txt","a")
    name     = input("Enter your name: ")
    surname  = input("Enter your surname: ")
    age      = input("Enter your age :")
    password = input("Enter your password: ")
    userName = name[0:3] + age
    file.write(userName+":"+password+":"+name+":"+surname+":"+age+"\n")
    file.close

def studentlogin():
    global userName
    print("Enter login details: ")
    UserName = input("Enter login details")
    password = input("Enter Your password")
    file = open("Users.txt","r")
    for eachline in file:
        user,pW,name,surNam,age=eachline.split(":")
        print("welcome",name)
        return mainMenu()
    print("Incorrect details")
    defExitOption()





defExitOption()
newUser()
startUpMenu()
studentlogin()
teacherLogin()

