from .Bank import BankAccount

account = BankAccount()



admin_password = 'Adminpermit'
# The users interface for the bank
print('Login......')
enter_password = input('Enter password:')

if enter_password == admin_password: 
    print('Welcome Admin\n')
    todo = input('What will you like to do?: ')
    print('1: Create an account\n')
    if todo == 1: 
        holders_name = input("Enter Holders name:")
        Account_number = input("Enter account number:")
        balance = input("Enter initial deposit:")
        Age = input("Enter Age: ")
        next_of_kin = input('Enter Next of Kin: ')
        password = input('Enter an initial password: ')
        email = input('Enter an email address')
        # creating the account using the account method
        


print('You are not permitted to do this operations')