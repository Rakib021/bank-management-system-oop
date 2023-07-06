class BankAccount:
    def __init__(self):
        self.accounts= {}
        
    def create_account(self,name):
        self.name = name
        if name not in self.accounts:
            self.accounts[name] = {"balance" :0 ,"transaction" :[]}
            print(f"---->account created successfully for {name}<-----")
            
        else:
            print("----->Already have an account for this name<-----")
            
    def deposit(self,name,amount):
        self.name = name
        self.amount = amount
        
        if name in self.accounts:
            self.accounts[name]["balance"] += amount
            self.accounts[name]["transaction"].append(f"deposited : {amount}")
            print(f"{amount} deposited successfully for {name}'s account")
            
        else:
            print("account does not exits")
            
    def withdraw(self,name,amount):
            self.name = name
            self.amount = amount
        
            if name in self.accounts:
               if self.accounts[name]["balance"] >=amount:
                  self.accounts[name]["balance"] -=amount
                  self.accounts[name]["transaction"].append(f'withdraw money :{amount}')
               else:
                    print("Your account is faka faka...please deposited some money")
            else:
                print("account doesnot exits")
                
    def check_bal(self,name):
        if name in self.accounts:
            balance = self.accounts[name]["balance"]
            print(f"available balance for {name} : {balance}")
        else:
            print("account doesn't exits")
            
    def transfer(self,sender,receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        
        if sender in self.accounts and receiver in self.accounts:
            if self.accounts[sender]["balance"] >=amount:
                self.accounts[sender]["balance"] -=amount
                self.accounts[sender]["transaction"].append(f"transferrred {amount} to {receiver}")
                self.accounts[receiver]["balance"] +=amount
                self.accounts[receiver]["transaction"].append(f"received {amount} from {sender}")
                print(f"{amount} transferred successfully from {sender} to {receiver} account")
            else:
                print("Insufficient balance")
        else:
            print("Both accounts does not exit")
            
    def transaction_history(self, name):
        if name in self.accounts:
            transaction = self.accounts[name]["transaction"]
            print(f"Transaction history for {name}:")
            for transaction in transaction:
                print(transaction)
        else:
            print("Account does not exist.")
            
    def take_loan(self, name):
        if name in self.accounts:
            total_amount = self.accounts[name]["balance"]
            loan_amount = total_amount * 2
            self.accounts[name]["balance"] += loan_amount
            self.accounts[name]["transaction"].append(f"Loan taken: {loan_amount}")
            print(f"{loan_amount} loan taken successfully by {name}.")
        else:
            print("Account does not exist.")
            
    def get_total_balance(self):
            total_balance = sum(account["balance"] for account in self.accounts.values())
            return total_balance

    def get_total_loan_amount(self):
        total_loan_amount = sum(account["balance"] for account in self.accounts.values())
        return total_loan_amount
    
        
class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, user_id):
        if user_id in self.bank.accounts:
            print("Account already exists.")
        else:
            self.bank.create_account(user_id)
            print(f"Account {user_id} created successfully.")


    def check_total_balance(self):
        total_balance = self.bank.get_total_balance()
        print(f"Total balance of the bank: ${total_balance}.")

    def check_total_loan_amount(self):
        total_loan_amount = self.bank.get_total_loan_amount()
        print(f"Total loan amount of the bank: ${total_loan_amount}.")

    def enable_loan_feature(self):
            self.loan_feature_enabled = True
            print("Loan feature enabled.")

    def disable_loan_feature(self):
        self.loan_feature_enabled = False
        print("Loan feature disabled.")

