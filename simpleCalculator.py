class operate:
    def addition(self,num1,num2):
        print('\nthe result is: '+str(num1+num2)+'\n')

    def subtraction(self,num1,num2):
        print('\nthe result is: '+str(num1-num2)+'\n')

    def multiplication(self,num1,num2):
         print('\nthe result is: '+str(num1*num2)+'\n')

    def division(self,num1,num2):
        try:
         print('\nthe result is: '+str(num1/num2)+'\n')
        except: print('\nError occur division on zero')

    def remaining(self,num1,num2):
         print('\nthe result is: '+str(num1%num2)+'\n')

while True:
    operation=input('Enter 1 for addition,2 for subtraction,3 for multiplication,4 for division,5 for remaining, 6 for exit: ')
    if operation == str(6): break

    number1=int(input('\nEnter first number: '))
    number2=int(input('\nEnter second number: '))
    result = operate()
    if operation == str(1):
        result.addition(number1,number2)

    elif operation == str(2):
        result.subtraction(number1,number2)

    elif operation == str(3):
        result.multiplication(number1,number2)

    elif operation == str(4):
        result.division(number1,number2)

    else:
         result.remaining(number1,number2)


    con=input('enter 1 to try again, 0 for exit:\n')
    if con == str(1):
        continue
    else: break

