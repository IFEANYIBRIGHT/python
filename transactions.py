balance = 0.0
transactions = []

while True:
    menu = """
WELCOME CUSTOMER, WHAT WOULD YOU LIKE TO DO TODAY?
1. Deposit Money
2. Withdraw Money
3. Show Transaction History
4. Exit The Program
"""
    print(menu)

    choice = int(input("What do you want to do? "))

   
    if choice == 1:
        deposit = float(input("How much do you want to deposit? "))
        balance += deposit
        transactions.append(f"Deposited: {deposit}")
        print(f"You deposited ${deposit}. New Balance: ${balance}")

 
    elif choice == 2:
        withdraw = float(input("How much do you want to withdraw? "))
        if withdraw > balance:
            print("Insufficient funds!")
            transactions.append(f"Failed withdrawal: {withdraw}")
        else:
            balance -= withdraw
            transactions.append(f"Withdrew: ${withdraw}")
            print(f"You withdrew {withdraw}. New Balance: {balance}")

  
    elif choice == 3:
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for money in transactions:
                print("-", money)

    
    elif choice == 4:
        print(f"Final Balance: {balance}")
        print("Thank you for using Transaction Log App!")
        break

    else:
        print("Invalid choice. Please try again.")

        

       

