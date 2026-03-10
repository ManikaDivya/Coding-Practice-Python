def atm_with_params(balance, withdrawal):
    if withdrawal <= balance:
        balance -= withdrawal
        print(f"Withdrawal successful! Remaining balance: {balance}")
    else:
        print("Insufficient balance!")

balance = float(input("Enter your current balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

atm_with_params(balance, withdrawal)
