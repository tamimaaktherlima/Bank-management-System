class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = []  # all accounts er database
        self.total_money = []

    def create_account(self,account):
        self.accounts.append(account)
        print (f'{account.name} is created Account Successfully !! ')

    def find_account(self,acc_name):
        for nm in self.accounts:
            if nm.name.lower() == acc_name.lower():
                return nm
            
            return None

    def delete_account(self,account_name):
        ac = self.find_account(account_name)
        if ac :
            self.accounts.remove(ac)
            print (f'{ac.name}, this account is Deleted Successfully !')
        else:
            print (f'{account_name}, this account is not Found !')
        
    def view_account(self):
        print ("*******User Account List !!*******")
        for acc in self.accounts:
            print (f'{acc.name} {acc.email} {acc.address} {acc.phone} {acc.account_number} {acc.account_types} {acc.gender}')
