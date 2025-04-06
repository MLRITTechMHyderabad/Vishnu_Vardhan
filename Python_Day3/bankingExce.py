class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self):
        self.balance=10000
    def withdraw(self,amount):
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("Enter amount in number")
            if amount<0:
                raise ValueError("Negative withdrawal not allowed")
            if (amount>self.balance):
                raise InsufficientFundsError("Insuffient balance")
            self.balance-=amount
            return f"Withdrawal Successful Remaining Balance is : {self.balance}"
        except ValueError as e:
            return e
        except InsufficientFundsError as ie:
            return ie

c=BankAccount()
try:
    amount=float(input("Enter The Amount"))
    print(c.withdraw(amount))
except Exception as e:
    print(e)
