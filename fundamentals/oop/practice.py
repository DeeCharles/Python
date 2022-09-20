class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []#This now has one bank account which is defined in 25
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)#New instance goes into line 5

    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
            print(sum)
        return sum
account_type=BankAccount(0.02,300)
print(account_type.balance,account_type.int_rate)
BankAccount.change_bank_name("Trust Bank")
print(BankAccount.bank_name)

print(BankAccount.all_accounts[0].balance)