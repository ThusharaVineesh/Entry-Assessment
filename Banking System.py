#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Bank:
    def __init__(self,username,pin_number):
        self.u=username
        self.p=pin_number
        self.balance=0
    def logininfo(self):
        self.u=input('Enter yourname ')
        self.p=input('Enter a Atm Pin ')
        address=input('Enter your address ')
        pancardnumber=input('Enter your PAN card number')
        mobilenumber=input('Enter your mobile number ')
        adharnumber=input('Enter your Adhar')
    def deposition(self):
        depositing_amount=int(input('Enter the amount = '))
        self.balance+=depositing_amount
        print(f'Amount of {depositing_amount} credited to your account successfully ,your current balance is{self.balance}')
    def withdrawel(self):
        withdrawying_amount=int(input('Enter the amount = '))
        if withdrawying_amount<=self.balance:
            self.balance-=withdrawying_amount
            print(f'Amount of {withdrawying_amount} debited from your account successfully ,your current balance is{self.balance}')
        else:
            print('Insufficient Amount')
def main():
    print(' Heloo Welcome to State bank of india ')
    function=int(input('if you are a new user please choose 1\n if your are a exisiting user please choose 2'))
    if function==1:
        username=input('Enter yourname ')
        pin_number=input('Enter a Atm Pin ')
        address=input('Enter your address ')
        pancardnumber=input('Enter your PAN card number')
        mobilenumber=input('Enter your mobile number ')
         
    elif function==2:
                username=input('Enter your user name')
                pin_number=input('Enter your pin_number')
    user=Bank(username,pin_number)
    selection=int(input('select 1 for deposit\nselect 2 for withdraw '))
    if selection==1:
            user.deposition()
    elif selection==2:
            user.withdrawel()
    print('Thank you for using SBI')
                        
                 
                
        
        
        


# In[5]:


main()


# In[ ]:




