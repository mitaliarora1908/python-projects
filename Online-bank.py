def create_account(i,l,acct_dict):
    print('CREATING A NEW ACCOUNT')
    acct_no = i
    acct_name = input("Enter your name :- ").strip()
    error_entry1 = True
    while error_entry1:
        try:
            acct_type = int(input("(1)Savings Account   (2)Current Account\nChoose the type of account :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option")
            continue
        else:
            error_entry1 = False
    if acct_type in (1,2):
        acct_address = input("Enter your residential address :- ").strip()
        acct_balance = 0
        acct_dict[acct_no] = [acct_name,acct_type,acct_address,acct_balance]
        print("**************ACCOUNT CREATED SUCCESSFULLY*************************\nYour account number is :- {}".format(acct_no))
        l.append(i)
        i=i+1
        continue_service(i, l, acct_dict)
    else:
        print("INVALID OPTION ENTERED...TRY AGAIN\n")
        create_account(i,l,acct_dict)

def access_account(i, l, acct_dict,acct_number):
    error_entry3 = True
    while error_entry3:
        try:
            acct_number = int(input("Enter your account number :- "))
        except ValueError:
            print("Account number should be valid integer. Please enter your valid account number.")
            continue
        else:
            error_entry3 = False
    if acct_number not in l:
        print("You are not a user of our bank.. Please register yourself by creating an account in our bank first")
        error_entry4 = True
        while error_entry4:
            try:
                try_again = int(input("(1)Create an account ?   (2)Quit the application\nYour Choice :- "))
            except ValueError:
                print("You have to enter a valid integer value for this option")
                continue
            else:
                error_entry4 = False
        if(try_again==1):
            create_account(i, l, acct_dict)
        elif(try_again==2):
            quit_application()
        else:
            print("INVALID OPTION ENTERED...TRY AGAIN\n")
            access_account(i, l, acct_dict,acct_number)
    else:
        error_entry5= True
        while error_entry5:
            try:
                acct_action = int(input("(1)Check Balance  (2)Deposit Money  (3)Withdraw Money  (4)Go to Another account  (5)Quit Application\nYour Choice :- "))
            except ValueError:
                print("You have to enter a valid integer value for this option")
                continue
            else:
                error_entry5 = False
        if(acct_action == 1):
            check_balance(acct_number,i, l, acct_dict)
        elif(acct_action == 2):
            deposit_money(acct_number,i, l, acct_dict)
        elif(acct_action == 3):
            withdraw_money(acct_number,i, l, acct_dict)
        elif(acct_action == 4):
            access_account(i, l, acct_dict,acct_number)
        elif(acct_action == 5):
            quit_application()
        else:
            print("INVALID OPTION ENTERED...TRY AGAIN\n")
            access_account(i, l, acct_dict,acct_number)
def check_balance(acct_number,i, l, acct_dict):
    print("Account balance of account no {} = {}".format(acct_number,acct_dict[acct_number][3]))
    continue_service(i, l, acct_dict)

def deposit_money(acct_number,i, l, acct_dict):
    error_entry7 = True
    while error_entry7:
        try:
            deposit_amount = int(input("Enter the amount of money to be deposited in your account no {} :- ".format(acct_number)))
        except ValueError:
            print("You have to enter a valid integer value for this option")
        else:
            error_entry7 = False
    acct_dict[acct_number][3] = acct_dict[acct_number][3]+deposit_amount
    print("DEPOSIT SUCCESSFUL\nNew balance of account no {} = {}".format(acct_number,acct_dict[acct_number][3]))
    continue_service(i, l, acct_dict)

def withdraw_money(acct_number,i, l, acct_dict):
    error_entry9 = True
    while error_entry9:
        try:
            withdrawn_amount = int(input("Enter the amount of money to be withdrawn from your account :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option")
            continue
        else:
            error_entry9 = False

    balance = (acct_dict[acct_number][3] - withdrawn_amount)
    if (balance<0):
        print("Your account balance is lower than your requested withdraw amount.. Withdrawal failed")
    else:
        acct_dict[acct_number][3] = balance
        print("WITHDRAWAL SUCCESSFUL\nNew balance of account no {} = {}".format(acct_number, acct_dict[acct_number][3]))
    continue_service(i, l, acct_dict)

def continue_service(i, l, acct_dict):
    error_entry10 = True
    while error_entry10:
        try:
            further_action = int(input("(1)Continue with other services ?   (2)Quit Application ?\nYour Choice :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option")
            continue
        else:
            error_entry10 = False
    if(further_action==1):
        old_user(i, l, acct_dict)
    elif(further_action==2):
        quit_application()
    else:
        print("INVALID OPTION ENTERED...TRY AGAIN\n")
        continue_service(i, l, acct_dict)

def quit_application():
    print("***********************************************")
    print('Thanks for visiting our online banking website')
    print("***********************************************")
    exit

def old_user(i, l, acct_dict):
    error_entry11 = True
    while error_entry11:
        try:
            acct_number = int(input("Enter your account number :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option")
            continue
        else:
            error_entry11 = False
    if acct_number not in l:
        print("You are not a user of our bank.. Please register yourself by creating a valid account in our bank first")
        error_entry12 = True
        while error_entry12:
            try:
                try_again = int(input("(1)Create an account ?   (2)Quit the application\nYour Choice :- "))
            except ValueError:
                print("You have to enter a valid integer value for this option")
                continue
            else:
                error_entry12 = False
        if(try_again==1):
            create_account(i, l, acct_dict)
        elif(try_again==2):
            quit_application()
        else:
            print("Invalid Option Entered.. Quiting The Application")
            quit_application()
    else:
        error_entry13 = True
        while error_entry13:
            try:
                user_option = int(input("(1)Create another account with us   (2)Access existing account   (3)Quit Application\nYour choice :- "))
            except ValueError:
                print("You have to enter a valid integer value for this option")
                continue
            else:
                error_entry13 = False
        if (user_option == 1):
            create_account(i, l, acct_dict)
        elif (user_option == 2):
            access_account(i, l, acct_dict,acct_number)
        elif(user_option==3):
            print("Quiting Application")
            quit_application()
        else:
            print("INVALID OPTION ENTERED...TRY AGAIN\n")
            old_user(i, l, acct_dict)

def new_user(i, l, acct_dict):
    error_entry14 = True
    while error_entry14:
        try:
            new_user_option = int(input("(1)Create Account  (2)Quit Application\nYour Choice :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option")
            continue
        else:
            error_entry14 = False
    if (new_user_option == 1):
        create_account(i, l, acct_dict)
    elif (new_user_option == 2):
        quit_application()
    else:
        print("INVALID OPTION ENTERED...TRY AGAIN\n")
        new_user(i, l, acct_dict)

def main():
    print("************************************")
    print("---WELCOME TO OUR ONLINE BANKING SERVICES---")
    print("************************************\n")
    acct_dict = {}
    i = 1
    l = []
    error_entry15 = True
    while error_entry15:
        try:
            option = int(input("(1)Already a User of our bank?  (2)Not a User of our bank? (3)Quit Application\nYour choice :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option.. Please try again")
            continue
        else:
            error_entry15 = False
    if(option ==1):
        old_user(i, l, acct_dict)
    elif(option==2):
        new_user(i, l, acct_dict)
    elif(option==3):
        quit_application()
    else:
        print("INVALID OPTION ENTERED...TRY AGAIN\n")
        main()

if __name__ == "__main__":
    main()