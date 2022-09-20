name = input("Enter your username? \n ")
allowedUsers = ["Timothy", "Daniel", "Odun", "Peter"]
allowedPassword = ["timothy", "daniel", "odun", "peter"]



if name in allowedUsers:
    password = input("Enter your password? \n ")
    userId = allowedUsers.index(name)

    if password == allowedPassword[userId]:
        print(f"Welcome {name}")
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")



        selections = int(input("Please select an option: "))

        if selections == 1:
            print(f"You selected Withdrawal ")
            withdrawalAmount = int(input("How much do you want to withdraw? \n"))
            print(withdrawalAmount)
            print(f"Withdrawal successful!!!")


        elif selections == 2:
            print(f"You selected Cash Deposit")
            cashDepositAmount = int(input("How much do you want to deposit? \n"))
            print(cashDepositAmount)
            print(f"Cash Deposit successful!!!")


        elif selections == 3:
            print(f"You selected Complaint")
            complaint = (input("please kindly enter your Complaints? \n"))
            print(complaint)
            print(f"Complaint Delivered!!!")

        else:
            print("invalid option selected please try again")

    else:
        print("Password incorrect, please try again")
else:
    print("Name not found, please try again")





print(name)