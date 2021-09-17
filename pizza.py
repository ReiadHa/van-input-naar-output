from sys import intern

print('prijzen: ')
print('small pizza  = 5.5 eruo per pizza')
print('medium pizza = 8.5 euro per pizza')
print('larg  pizza  = 10.5 euro per pizza')

small  = float(input('Aantal small pizza: '))
medium = float(input('aantal medium pizaa: '))
larg   = float(input('Aanstal larg pizza: '))

smallpizza  = 5.5
mediumpizza = 8.5
largpizza   = 10.5

amount1= small 
amount2= medium
amount3= larg


factuur1 = ('totaal small pizza: ')  + str((small)*(smallpizza))


factuur2 = ('totaal medium pizza: ') + str((medium)*(mediumpizza))


factuur3 = ('totaal larg pizza: '  ) + str((larg)*(largpizza))

totaal   ='je factuur/ totaale bedrag is: ' + str((small)*(smallpizza)+(medium)*(mediumpizza)+(larg)*(largpizza))
print('---------------------------------------------')

print('aantal small pizza:'  + str(int(amount1)))
print(factuur1)

print('---------------------------------------------')

print('aantal medium pizza: ' + str(int(amount2)))
print(factuur2)

print('---------------------------------------------')

print('aantal larg pizza: '   + str(int(amount3)))
print(factuur3)

print('---------------------------------------------')


print(totaal)


