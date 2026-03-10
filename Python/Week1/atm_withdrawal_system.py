balance = float(input("Enter initial balance: "))

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        deposit = float(input("Enter deposit amount: "))
        balance += deposit
        print("Amount Deposited Successfully")

    elif choice == 3:
        withdraw = float(input("Enter withdrawal amount: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid Choice")
