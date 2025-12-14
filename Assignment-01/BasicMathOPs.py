a: int = 0
b: int = 0

x: str = input('Enter the first number: ')
while x.isdigit() == False:
    x = input('Enter a valid First number: ')

y: int = input('Enter the second number: ')
while y.isdigit() == False:
    y = input('Enter the valid second number: ')

a= int(x)
b = int(y)

print('============ RESULTS ============')
print('Addition =',a+b)
print('Subtraction =',a-b)
print('Multiplication =',a*b)
if b != 0:
    print('Division =',a/b)
else:
    print('Division = Infinity')


