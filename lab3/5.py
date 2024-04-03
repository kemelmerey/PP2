#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
#Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, 
#and test to make sure the account can't be overdrawn.

#class Account:     pass
class bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 
    
    def deposit(self, sum):
        self.balance = self.balance + sum
        print(f"deposit of {sum} accepted. New balance: {self.balance}")

    def withdraw(self, sum):
        if sum <= self.balance:
            self.balance = self.balance - sum
            print(f"Withdraw of {sum} accepted. New balance: {self.balance}")
        else:
            print("not enough money")

Bank = bank_account(input("owner is: "), abs(float(input("The balance is:"))))

Bank.deposit(float(input("Write the sum you want to deposit:" )))

Bank.withdraw(float(input("write the sum you want to withdraw:" )))