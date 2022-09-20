class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        self.balance-=amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-5
        return self
        
    def display_account_info(self):
        self.balance += self.balance*self.int_rate
        print("Balance: ",self.balance)
        return self
                
    # def yield_interest(self):
    #     if self.balance>0:
    #         self.balance += self.balance*self.int_rate
    #     return self

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        #self.account is an instance of BankAccount class and an attribute of the User class.
        self.account={
            "savings":BankAccount(int_rate=0.03,balance=0),
            "checking":BankAccount(int_rate=0.03,balance=0)
            } 
        


    def make_deposit(self,amount,account_type):
        self.account[account_type].deposit(amount)
        return self


    def make_withdrawal(self,amount,account_type):
        self.account[account_type].withdraw(amount)
        return self

    def display_account_info(self):
        print(f"Savings: {self.account['savings'].balance}")
        print(f"Checking: {self.account['checking'].balance}")
        print(self.name)
        return self

    def transfer_money(self,amount,account_type,other_user):
        if self.account[account_type].balance>amount:
            self.account[account_type].withdraw(amount)
            other_user.account[account_type].deposit(amount)
        else:
            print("You broke")
        return self



#instance of User class
user1=User("Jane Doe","jdoe@email.com")
#print(user1.name,user1.email)
user2=User("Kevin Doe","kd@email.com")


#invoking functions
user1.display_account_info().make_deposit(100,"savings").display_account_info().transfer_money(25,"savings",user2).display_account_info()
#user2.make_withdrawal(300,"savings").display_account_info().transfer_money(100,"checking",user1)

#print(user1.account.balance,user1.account)
#user1.display_account_info()
user2.display_account_info()





