# START
# IMPORT TIME LIB
import time
import pyperclip as pc
# SET PASSWORD MANAGERING FUNCTION;
def Password_Manager() :
    # IMPORT MOD FROM LIBS
    from random import choice
    from string import ascii_letters , digits
    from datetime import datetime
    # PRINT HELP
    print("""
 _____________________________________________________________
| * _______________________________________________________ * |
|  | *          Enter Command Number For Start           * |  |
|  |   *************************************************   |  |
|  |  1 >> Make Easy Password     (just Numbers)           |  |
|  |  2 >> Make Normall Password  (Numbers and letters)    |  |
|  |  3 >> Make Hard Password     (All Characters)         |  |
|  |  4 >> Add Old Password       (Need An Old Password)   |  |
|  |  5 >> Show Passwords         (Print all Passwords)    |  |
|  |__2022____________________________________________1.0.0|  |
|_____________________________________________________________|
""")
    # SET PASSWORD MAKER FUNCTION;
    def make_password(level) :
        if level == 1 :
            char = digits
        elif level == 2 :
            char = digits + ascii_letters
        elif level == 3 :
            char = """qwertyuiopasdfghjklzxcvbnm1234567890-=[];'\,./`~!@#$%^&*()_+}{POIUYTREWQASDFGHJKL:"|?><MNBVCXZ|"""
        else :
            print ("Password Lever is not defind;\nTry again layter;")
        password = """"""
        passlen = int(input("Enter password len \n~/:>  "))
        passtitle = str(input("Enter password title \n~/:>  "))
        while len(password) < passlen :
            password += choice(char)
        passline = "Title : " + passtitle
        while len(passline) <  33 :
            passline += " "
        passline += "|  Password : " + str(password)
        while len(passline) < 68 :
            passline += " "
        passline += "| Time : " + str(datetime.now())
        PassFile = open("Passwords.txt" , "a+")
        PassFile.write(passline + "\n")
        PassFile.close()
        pc.copy(password)
        print ("|*********************\n|  " + password + " \n**********************")
    # RUN THE TOOLS
    tool = int(input("~/:>  "))
    if tool == 1 or 2 or 3 or 4 :
        if tool == 1 :
            make_password(tool)
        elif tool == 2 :
            make_password(tool)
        elif tool == 3 :
            make_password(tool)
        elif tool == 4 :
            passtitle = str(input("Enter password title \n~/:>  "))
            password = str(input("Enter password \n~/:>  "))
            passline = "Title : " + passtitle
            while len(passline) < 33 :
                passline += " "
            passline += "|  Password : " + str(password)
            while len(passline) < 68 :
                passline += " "
            passline += "| Time : " + str(datetime.now())
            PassFile = open("Passwords.txt" , "a+")
            PassFile.write(passline + "\n")
            PassFile.close()
        elif tool == 5 :
            pass
            PasswordFile = open("Passwords.txt" , "r")
            print ("""########################################################################################################""")
            print (PasswordFile.read())
            print ("""########################################################################################################""")
        else :
            print("Command is not definde;")
    else :
        print("Command is not definde;")
Password_Manager()
again = int(input("For run again enter 1 and For exit enter 0; \n~/:>  "))
while again == 1 :
    Password_Manager()
    again = int(input("For run again enter 1 and For exit enter 0; \n~/:>  "))
print("\nGood Bye;\n")
time.sleep(1)