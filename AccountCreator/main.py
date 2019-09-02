from account import *
import sys

def intro():
  print(
'''
             ________________________________________________
            /                                                \\
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:> _  WELCOME :) :)                   |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \\_________________________________________________/
                   \\___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
'''
)
'''
------------------------------------------------------------------------------------------------
'''
def display_menu():
  print('''
***************************************
* CHOOSE ONE OF THE FOLLOWING OPTIONS *
* 1 -> CREATE ACCOUNT                 *
* 2 -> DELETE ACCOUNT                 *
* 3 -> EXIT                           *
****************************************
''')
  c = int(input('Enter your choice here : '))
  if c == 1:
    create_account()
  elif c == 2:
    delete_account()
  else:
    sys.exit()

'''
------------------------------------------------------------------------------------------------
'''

def create_account():
  print(
''' 
YOU CAN CREATE AN ACCOUNT BY 
FILLING OUT THE FOLLOWING 
FIELDS.
''')
  name = input('Name : ')
  email = input('Email address : ')
  verif_question = input('Verification question : ')
  birth_date = input('Enter your date of birth : ')
  password = input('Password : ')
  phone_num = int(input('Phone number : '))
  age = int(input('Age : '))

  temp = Account(name,email,verif_question,birth_date,password,phone_num,age)
  display_account(temp)

  write_file(temp)
  display_menu()

'''
------------------------------------------------------------------------------------------------
'''

def delete_account():
  name = input('Enter the name on the account you want to delete : ')
  with open('account.txt','wb+') as act:
    for line in act:
      if act.name != name:
        act.write(line)

'''
------------------------------------------------------------------------------------------------
'''

def write_file(obj):
  with open('account.txt','a+') as act:
    act.write(str(obj))

'''
------------------------------------------------------------------------------------------------
'''

def read_file():
  with open('account.txt','r') as act:
    file = act.read()
'''
------------------------------------------------------------------------------------------------
'''

def display_account(obj):

  print('\n\n\n--------------------------------------------------')
  print('Account info :')
  print('Name :', obj.name)
  print('Email :', obj.email)
  print('Verification question :', obj.verif_ques)
  print('Date of birth :', obj.birth_date)
  print('Password :', obj.password)
  print('Phone number :', obj.phone_num)
  print('Age :', obj.age)
  print('--------------------------------------------------')

'''
------------------------------------------------------------------------------------------------
'''

if __name__ == '__main__':
  intro()
  display_menu()
