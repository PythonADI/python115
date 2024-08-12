class Transaction:
    def __init__(self, from_account, to_account, amount) -> None:
        self.from_account = from_account
        self.to_account = to_account
        try:
            self.from_account.transfer(self.to_account, amount)
        except Exception as e:
            raise ValueError('Transaction failed', e)
        self.amount = amount


class Account:
    accounts_created = 0 # static attribute

    def __init__(self) -> None:
        self.id = Account.accounts_created
        self.balance = 0
        Account.accounts_created += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
    
    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


accounts = [
    Account(),
    Account(),
    Account()
]
for account in accounts:
    account.deposit(7000)
    print(account.id)
    print(account.balance)

print('Next id', Account.accounts_created)

transactions = [
    Transaction(accounts[0], accounts[1], 6000),
]

print(accounts[0].balance, accounts[1].balance)