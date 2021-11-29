from cv2 import cv2
import time
import os


def showWebcam():
    # Access the cascdeclassifier
    face_cascde = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # sets window size 640X640
    wCam, hCam = 640, 640

    # access first webcam avalible
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, wCam)
    cap.set(4, hCam)

    while True:
        success, img = cap.read()

        # converts video feed to to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascde.detectMultiScale(gray, 1.3, 5)

        # sets square around face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("Panda Protection", img)
        cv2.waitKey(50)


clear = lambda: os.system('cls')
DataBase = {}


def printIntroPage():
    print("\tPanda Protection")
    print("1) Create Account")
    print("2) Login")
    print("3) Exit")


def printMainPage():
    print("\tMain Menu")
    print("1) Open Webcam")
    print("2) Settings")
    print("3) Exit")


def printSettingsPage():
    print("\tUser Settings")
    print("1) Change Username")
    print("2) Change Password")
    print("3) Add New User")
    print("4) Return to Main Menu")


def introMenu():
    clear()
    printIntroPage()

    userChoice = int(input("Enter Choice: "))

    if (userChoice == 1):
        createAccount()
    elif (userChoice == 2):
        login()
    elif (userChoice == 3):
        exit()


def createAccount():
    clear()
    print("\tCreate Account")

    username = input("Enter Username: ")
    password = input("Enter password: ")

    checkVal = checkUserInfo(username)

    if (checkVal):
        DataBase[username] = password
        print("1) Submit")
        print("2) Exit")

        userChoice = int(input("Enter Choice: "))
        if (userChoice == 1):
            introMenu()
        else:
            exit()

    else:
        print("Username must be above 6 characters. Try Again")
        time.sleep(2)
        createAccount()


def login():
    clear()
    print("\tLogin")



    username = input("Enter Username: ")
    password = input("Enter password: ")
    loginVal = verifyPassword(username, password)

    if (login):
        home()
    else:
        print("Incorrect Username or Password\n")
        time.sleep(2)

        print("1) Try again")
        print("2) Back to Main Menu")
        userChoice = int(input("Enter Choice: "))

        if (userChoice == 1):
            login()
        else:
            introMenu()


def checkUserInfo(username):
    if (len(username) < 6):
        return False
    else:
        return True


def verifyPassword(username, password):
    checkUsername = DataBase.get(username)
    if (checkUsername == None):
        return False
    else:
        if (checkUsername == password):
            print("Verified")
            return True
        else:
            return False


def home():
    clear()
    printMainPage()

    userChoice = int(input("Enter Choice: "))

    if userChoice == 1:
        openCamera()
    elif userChoice == 2:
        userSettings()
    elif userChoice == 3:
        exit()


def openCamera():
    showWebcam()


def userSettings():
    clear()
    printSettingsPage()

    userChoice = int(input("Enter Choice: "))

    if userChoice == 1:
        clear()
        print("\tChange Username")
        temp = input("Enter your old username: ")

        if temp in DataBase:
            tempNew = input("Enter new username: ")
            DataBase[tempNew] = DataBase.pop(temp)
            print("Username has been changed to: ", tempNew)
            time.sleep(2)
            userSettings()
        else:
            print("Username not found...")
            time.sleep(2)
            userSettings()

    if userChoice == 2:
        clear()
        print("\tChange Password")
        temp = input("Enter Username: ")

        if temp in DataBase:
            tempNew = input("Enter new password: ")
            DataBase[temp] = tempNew
            print(DataBase)
            print("Password has been changed to: ", tempNew)
            time.sleep(2)
            userSettings()
        else:
            print("Username not found...")
            time.sleep(2)
            userSettings()

    if userChoice == 3:
        clear()
        print("\tAdd New User")

        username = input("Enter username: ")
        password = input("Enter password: ")

        DataBase[username] = password
        print("New user has been added...")
        print(DataBase)
        time.sleep(2)
        userSettings()

    if userChoice == 4:
        home()


introMenu()
