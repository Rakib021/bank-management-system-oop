class Bank:
    def __init__(self):
        self.accounts= {}
        
    def create_account(self,name):
        self.name = name
        if name not in self.accounts:
            self.accounts[name] = {"balance" :0 ,"transaction" :[]}
            print(f"---->account created successfully for {name}<-----")
            
        else:
            print("-----Already have an account for this name-----")
            
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
            
    
        
        
        
            