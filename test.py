from datetime import *

def makeCalc(moment, birth, event):
    today = datetime.now()
    unk = ((birth * moment) - event) / (1-moment)
    return unk

numero = float(0.25)
today = datetime.now()
new_date_1 = today - datetime(1987, 6, 26)
new_date_2 = today - datetime(2010, 5, 30)

valor = makeCalc(numero, new_date_1, new_date_2)

print(valor)