class Bank:
    def __init__(self):
        self.accounts= {}
        
    def create_account(self,name):
        if name not in self.accounts:
            self.accounts[name] = {"balance" :0 ,"transaction" :[]}
            print(f"---->account created successfully for {name}<-----")
            
        else:
            print("-----Already have an account for this name-----")
            