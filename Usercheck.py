import sqlite3
import csv
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def quit_application():
    print("***********************************************")
    print('Thanks for visiting')
    print("***********************************************")
    exit()


def writetodb(log_in,pwd):
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tb_user (login,cryptographic_password,access_count) values ('{}','{}',0);".format(log_in, pwd))
    cursor.execute("COMMIT;")
    cursor.close()
    connection.close()

def encryptpassword(pwd):
    code_dict = {'A':'T','B':'I','C':'M','D':'E','E':'O','F':'D','G':'A','H':'N','I':'S','J':'F','K':'R',
                 'L':'B','M':'C','N':'G','O':'H','P':'J','Q':'K','R':'L','S':'P','T':'Q','U':'U','V':'V',
                 'W':'W','X':'X','Y':'Y','Z':'Z','0':'9','1':'8','2':'7','3':'6','4':'5','5':'4','6':'3',
                 '7':'2','8':'1','9':'0'}
    newpassword=''
    for i in pwd:
        newpassword += str(code_dict[(i.upper())])
    return newpassword

def newuser():
    # Creating New User
    print("CREATING YOUR ACCOUNT\n")
    log_in = input("Enter your email: ")
    if (check_email(log_in) == True):
        pwd = input("Enter an alphanumeric password <password is case insensitive> : ")
        if pwd.isalnum():
            encpwd = encryptpassword(pwd)
            writetodb(log_in, encpwd)
            print("User details loaded in Database")
            print("Please select further tasks to be performed")
            menu()
        else:
            print("Only alphanumeric password is allowed... Please try again")
            newuser()
    else:
        print("Invalid email ID format entered... Please try again")
        newuser()


def take_backup():
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    cursor.execute("select * from tb_user;")
    alldata = cursor.fetchall()
    try:
        with open('usersdb-backup.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['user_id', 'login', 'cryptographic_password', 'access_count'])
            writer.writerows(alldata)
    except PermissionError:
        print("Sorry..Unable to take back up of the file due to permission issues")
    else:
        print("Hot backup stored successfully\n")
    cursor.close()
    connection.close()

def check_email(email):
    if (re.match(regex,email)):
        return True
    else:
        return False

def olduser():
    log_in = input("Enter your email: ")
    if (check_email(log_in) == True):
        pwd = input("Enter your alphanumeric password <password is case insensitive> : ")
        if pwd.isalnum():
            encryptpwd = encryptpassword(pwd)
            connection = sqlite3.connect("user.db")
            cursor = connection.cursor()
            cursor.execute("SELECT login,access_count FROM tb_user where login = '{}' and cryptographic_password = '{}' ;".format(log_in,encryptpwd))
            check = cursor.fetchall()
            if not check:
                print("Incorrect details entered..Redirecting to the main menu")
                menu()
            else:
                cursor.execute("UPDATE tb_user set access_count = access_count+1 where login = '{}' and cryptographic_password = '{}';".format(log_in, encryptpwd))
                cursor.execute("COMMIT;")
                cursor.execute("SELECT login,access_count FROM tb_user where login = '{}' and cryptographic_password = '{}' ;".format(log_in,
                                                                                                                encryptpwd))
                results = cursor.fetchall()
                print("Please find below your user email ID and number of logins\n")
                for r in results:
                    print('EMAIL ID : {}'.format(r[0]))
                    print("NO OF LOGINS : {}".format(r[1]))
            cursor.close()
            take_backup()
        else:
            print("Only alphanumeric password is allowed... Please try again")
            olduser()
    else:
        print("Invalid email ID format entered... Please try again")
        olduser()
    menu()



def menu():
    error_entry = True
    while error_entry:
        try:
            option = int(input("(1)Old User  (2)New User  (3)Exit\nYour choice :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option.. Please try again")
            continue
        else:
            error_entry = False
    if(option == 1):
        olduser()
    elif(option == 2):
        newuser()
    elif(option == 3):
        quit_application()
    else:
        print("INVALID OPTION ENTERED...Please enter 1 for Old User and 2 for New User\n")
        menu()

def main():
    print("************************************")
    print("            WELCOME")
    print("************************************\n")
    menu()

if __name__ == "__main__":
    main()