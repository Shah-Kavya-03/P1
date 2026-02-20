class BankAccount:
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0
    def __init__(self,account_holder,initial_deposit):
        self.account_holder = account_holder
        self.balance = initial_deposit
        self.total_accounts +=1
        self.accont_number = self.total_accounts
        self.total_bank_balance += initial_deposit
    def deposit(self,amount):
        self.balance +=amount
        self.total_bank_balance += amount
        return self.balance
    def withdraw(self,amount):
        self.balance -=amount
        self.total_bank_balance -= amount
        return self.balance
    def display_account_info(self):
        print(f"Account Details:\nAccount Holder: {self.account_holder}\nAccount Number:{self.accont_number}\nBalance: {self.balance}\n")
def main():
    account = {}
    print(" Welcome To National Bank\n===========================")
    while True:
        choice = int(input("Choose Your Option:\n1. Create Account\n2. Deposit Amount\n3. Withdraw Amount\n4. Exit\n"))
        if choice == 1:
            name = input("Enter Account Holder Name: ")
            initial = int(input("Enter initial deposit amount: "))
            acc = BankAccount(name,initial)
            account[acc.accont_number] = acc
            print("Account created!!!")
            acc.display_account_info()
        elif choice == 2:
            accn = int(input("Enter account Number: "))
            amount = int(input("Enter Amount: "))
            if accn in account:
                balance = account[accn].deposit(amount)
                print(f"Rs. {amount} Deposited into Account no. {accn}\nCurrent Balance: {balance}\n")
        elif choice == 3:
            accn = int(input("Enter account Number: "))
            amount = int(input("Enter Amount: "))
            if accn in account:
                balance = account[accn].balance
                if balance >= amount:
                    balance = account[accn].withdraw(amount)
                    print(f"Rs. {amount} Withdrawed from Account no. {accn}\nCurrent Balance: {balance}\n")
                else:
                    print("Withdrawl amount is more than Account Balance\n")
        elif choice ==  4:
            print("Thank you For using National Bank !!!")
            break
        else:
            print("Wrong Choice. Choose again!!!")

if __name__ == "__main__":
    main()