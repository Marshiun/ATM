import UIOptions

def atm_menu(name):
    print("=== Automated Teller Machine ===")
    print("User: " + name)
    print("What would you like to do?")
    print("1.    Balance     ")
    print("2.    Deposit     ")
    print("3.    Withdraw    ")
    print("4.    Logout      ")

username_list=[]

print(username_list)

# REGISTRATION

print("          === Automated Teller Machine ===          ")
while True:
    username = input("Enter username to register: ")
    pin = input("Enter pin: ")
    if len(username) < 1 or len(username) > 10 or username in username_list:
        print("Username must be between 1 and 10 characters or Username is taken.")
    elif len(pin) != 4:
        print("Please enter 4 digits.")
    else:
        print("Username and password are OK!")
        break

username_list.append(username)

# print(username_list)

balance = 0
print(username + " has been registered with the starting balance of  $" + str(balance))

# LOGIN

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    username_to_validate = input("Enter username: ")
    pin_to_validate = input("Enter PIN: ")
    
    if username_to_validate == username and pin_to_validate == pin:
        print("Login Successful")
        break
    else:
        print("Invalid credential")

# UI DIRECTORY

while True: 
    atm_menu(username)
    option = input("Choose an option: ")
    if option == "1":
        UIOptions.show_balance(balance)
    elif option == "2": 
        balance = UIOptions.deposit(balance)
    elif option == "3": 
        balance = UIOptions.withdraw(balance)
    else: 
        UIOptions.logout(username)
        break              