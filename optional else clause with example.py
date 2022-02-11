'''for i in range(1):
 value = int(input('Enter an integer (-1 to break): '))
 print('You entered:', value)
 
 if value == -1:
     break
else:
 print('The loop terminated without executing the break')'''
 
 
# simple program to check the password in database using optional else clause
# To run this example program remove triple quotation's at beginning and ending of the program below
# try "teddy" as password. 
for i in range(1):
 value = input('Enter login password: ')
 print('You entered:', value)
  
 if value =='teddy':
     print("welcome to the app")
     break
else:
  print('you entered password not matched with password you set in database')