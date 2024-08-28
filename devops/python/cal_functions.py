def calculator(num1, opr, num2):

 if(opr == '+'):

return num1 + num2

elif(opr == '-'):

return num1 - num2

elif(opr == '/'):

if(num2 == 0):

return 'Number can\'t be divided by zero.'

return num1/num2

elif(opr == '*'):

return num1 * num2

else:

print('Invalid Operator.')

num1 = int(input('Enter first number: '))

num2 = int(input('Enter second number: '))

opr = input('Enter operation(+, - , *, /): ')

print(calculator(num1, opr, num2))