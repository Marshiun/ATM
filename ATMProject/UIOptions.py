#UI Options

def show_balance(balance):
    print("The Current Balance:",float(balance))

def deposit(balance): 
    amount = input("Enter amount to deposit ")
    return balance + float(amount)
    

def withdraw(balance): 
    amount = input("Enter amount to withdraw ")
    if balance < float(amount):
        print("Insufficient balance!")
        return float(balance)
    else:
        return balance - float(amount)

def logout(name): 
    print("Goodbye", name)          