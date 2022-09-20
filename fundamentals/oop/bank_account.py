class BankAccount:
    all_accounts = []

    def __init__(self): 
        self.balance=0
        self.int_rate=0.01
        BankAccount.all_accounts.append(self)
    

    def deposit(self, amount):
        self.balance+=amount
        return self
        #
        # print(self.balance)

    def withdraw(self, amount):
        self.balance-=amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-5
    #         print(self.balance)
            #return self.balance
        return self
        #else:
    #       return self
    #       print(self.balance)
    #       return self.balance

        
    def display_account_info(self):
        print("Balance: ",self.balance)
        return self
                
    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance*self.int_rate
        # else:
        return self
    #         print("Balance is negative", self.balance)
    #   return self
# Use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

account1=BankAccount()
account2=BankAccount()

account1.deposit(50).deposit(150).deposit(10).withdraw(25).yield_interest().display_account_info()
account2.deposit(500).deposit(700).withdraw(100).withdraw(250).withdraw(35).withdraw(45).yield_interest().display_account_info()

BankAccount.print_all_instances()