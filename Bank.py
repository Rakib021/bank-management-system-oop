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
            
   
        
        
            