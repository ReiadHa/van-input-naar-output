personen     = float(input('hoeveel personen zijn er? '))
entreekosten = 745
VRmin        = float(input('hoeveel minuten VR had je gespeeld? '))
VRkosten     = 37/5
eurowaarde   = ((personen) * (entreekosten) + (VRmin) * (VRkosten)) / 100

factuur      = 'je factuur is ' + str( eurowaarde )



print(factuur)