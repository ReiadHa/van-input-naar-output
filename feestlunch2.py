croissantjes = float(input('hoeveel criossant had je besteld '))
croikosten   = 39
stokbroden   = float(input('hoeveel stokbroden had je besteld '))
stokkosten   = 278
korting      = float(input('hoeveel korting bon had je gekregen '))
kortingen    = 50
eurowaarde = ((croissantjes)*(croikosten) + (stokbroden)*(stokkosten)-(korting)*(kortingen)) / 100
 

factuur      = 'je factuur is : '  + str(eurowaarde)

print(factuur)






