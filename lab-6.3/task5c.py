class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"Account balance for {self.name}: {self.balance}")


if __name__ == "__main__":
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(name, balance)
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")
