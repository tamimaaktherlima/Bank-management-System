from user import User,Account,Admin
from bank import Bank

mamar_bank = Bank('Mamur Bank')

print(f'***** Welcome To Islamic Limited Bank! *****')
print(f'1. Are you a User?')
print(f'2. Are you an Admin?')
print(f'3. Exit')
ch = int(input('Enter Your Choice : '))
if ch == 1:
    print(f'Welcome As a User!!!')
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    Address = input("Enter Your Address : ")
    Phone = input("Enter Your Phone Number : ")
    user = User(name=Name, email=Email,address=Address,phone=Phone)

    while True:
        print(f'****Welcome To Our Bank Mr./Mrs. {user.name}*****')
        print(f'1. View Balance')
        print(f'2. Deposite Balance')
        print(f'3. Withdraw Balance')
        print(f'4. Exit')

        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            User.view_balance(user)
        elif choice == 2:
            amount = float(input ('Enter Your Deposited Money : '))
            User.deposit(user,amount)
        elif choice == 3:
            amount = float(input ('Enter Your Withdral Money : '))
            User.withdraw(user,amount)
        elif choice == 4:
            break
        else:
            print(f'Invalid Input. Try Again!')

elif ch == 2:
    print('*****Welcome As a Admin!!******')
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    Address = input("Enter Your Address : ")
    Phone = input("Enter Your Phone Number : ")
    admin = Admin(name=Name,email=Email,address=Address,phone=Phone)

    while True:
        print(f'***Welcome {admin.name}***')
        print('1. Creat New Account')
        print('2. Delete An Account')
        print('3. View Account')
        print('4. View Total Amount')
        print('5. Exit')

        choice = int (input('Enter Your Choice : '))
        if choice == 1:
            Name = input('Enter Your Name : ')
            Email = input('Enter Your Email : ')
            Address = input('Enter Your Address : ')
            Phone = input('Enter Your Phone Number : ')
            Account_Number = input('Enter Your Account Number : ')
            Account_type = input('Enter Your Account Type : ')
            Gender = input('Enter Your Gender : ')
            account = Account(Name,Email,Address,Phone,Account_type,Gender,Account_Number)
            Admin.creat_account(admin,mamar_bank,account)
        elif choice == 2:
            Name = input("Enter Your Name : ")
            Admin.delete_account(admin,mamar_bank,Name)
        elif choice == 3:
            Admin.view_account(admin,mamar_bank)
        elif choice == 4:
            Admin.total_available_balance(admin)
        elif choice == 5:
            break
        else:
            print (f'Invalid Input. Try Again!')