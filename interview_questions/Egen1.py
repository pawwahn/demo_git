class Account:
    def __init__(self, account_id, initial_balance=0):
        self.account_id = account_id
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            return True 
        return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, initial_balance=0):
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = Account(account_id, initial_balance)
        return True

    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            return self.accounts[account_id].deposit(amount)
        return False

    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            return self.accounts[account_id].withdraw(amount)
        return False

    def rank_accounts(self):
        account_values = []
        for account_id, account in self.accounts.items():
            total_transactions = sum(
                int(t.split(": ")[1]) for t in account.transactions
            )
            account_values.append((account_id, total_transactions))
        return sorted(account_values, key=lambda x: x[1], reverse=True)

bank = Bank()
bank.create_account("A123", 1000)
bank.create_account("B456", 500)
bank.create_account("C789", 500)

bank.deposit("A123", 500)
bank.withdraw("A123", 200)
bank.deposit("B456", 300)
bank.withdraw("C789", 1500)

print("Ranking:", bank.rank_accounts())