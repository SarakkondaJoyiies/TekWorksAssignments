balance = 100000
class Bank:
    def deposit(self):
       amount=int(input("Enter the deposit amount:"))
       if amount<100 | amount>50000:
             if(amount%100!=0):
               print("Amount should be in multiples of 100")
               obj.deposit()
             else:
               print("Your deposit is valid")
               exit()
       else:
           print("Your deposit is invalid")
           obj.deposit()
    def withdraw(self):
       for i in range(1,4):
          withdrawl_amount=int(input("Enter the withdrawal amount:"))
          if(withdrawl_amount>=100):
             if(balance>500):
                if( withdrawl_amount>20000):
                   print("Transaction failed! Try again")
                   #obj.withdraw()
                else:
                   print("Transaction successful!")
                   updated_balance = balance - withdrawl_amount
                   print("Remaining balance:", updated_balance)
                   exit()
          else:
             print("Amount not valid!")
       exit()
    def viewOptions(self):
       print("1.Deposit")
       print("2.Withdraw")
       print("3.Bal Enquiry")
       print("0.EXIT")
       option=int(input("Choose your option:"))
       if option==1:
           obj.deposit()
       elif option==2:
           obj.withdraw()
    def validation(self):
       print("Welcome to ABC bank")
       for i in range(1, 4):
            pin = int(input("Enter the pin number:"))
            if pin!= 1234:
                if(i<3):
                  print("Please re-enter the pin")
                else:
                    print("Invalid pin,Try again later!")
                    break;
            else:
               obj.viewOptions()
obj = Bank()
obj.validation()
