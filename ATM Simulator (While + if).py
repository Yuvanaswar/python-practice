balance = balance=10000
while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice =int(input("Enter ur choice:"))
    if choice ==1:
        print("ur balance:",balance)
    elif choice ==2:
        amount=int(input("Enter the deposit amount:"))
        balance+=amount
    elif choice ==3:
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance-=amount
            print("Updated balance:",balance)
    elif choice ==4:
        print("Thx for usinf the ATM!!")
    else:
        print("Invalid choice!!")
        
