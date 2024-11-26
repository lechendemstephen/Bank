
class BankAccount: 
    def __init__(self):
        # creating an empty dictionary to add all account details 
        self.Accounts = {
                'name': {
                'account_number': 123334444, 
                'balance': 20444043, 
                'name': 'stephen Lechendem', 
                'Age': 29, 
                'Next_of_kin': 'Nkeng Clarence',
                'password': 'thisisapassword'
                }
        }
    # creating a method to create an account 
    def createAccount(self, holders_name: str, account_number: int, balance:int, age: int, next_of_kin: str, password:str, email:str): 
        # adding the new account to list of all accounts
        self.Accounts[holders_name] = {
            'Account_number': account_number, 
            'Balance': balance, 
            'Full Name': holders_name, 
            'Age': age, 
            'Next_of_kin': next_of_kin, 
            'password': password, 
            'email': email
        }
        if holders_name in self.Accounts: 
             self.Accounts.pop(holders_name)
             return print(f'an account already exist with the name: {holders_name}, created another account')
        return print(f'your account has been successfully created: {self.Accounts[holders_name]}')
    
        
account = BankAccount ()

account.createAccount('Asong Shanel', 3245421343, 30000, 35, 'Asah Alex', 'password123', 'asongshanel@gmail.com')

