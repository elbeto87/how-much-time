from datetime import datetime
from datetime import timedelta

def askDate(message):
    print (message)
    days_birth = int(input("Dias: "))
    while days_birth not in range(1, 32):
        days_birth = input("Ha ingresado un valor invalido, intente nuevamente")
    month_birth = int(input("Mes: "))
    while month_birth not in range(1, 32):
        month_birth = input("Ha ingresado un valor invalido, intente nuevamente")
    year_birth = int(input("Año: "))
    while year_birth not in range(1900, 2021):
        year_birth = input("Ha ingresado un valor invalido, intente nuevamente")
    date_birth = datetime(year_birth, month_birth, days_birth)
    return date_birth

def askMoment():
    resultado = {"1": 0.25, "2": 0.33, "3": 0.5, "4": 0.66, "5": 0.75}
    opcion = input("Ingrese si quiere calcular: \n [1] 1/4 de vida \n [2] 1/3 de vida \n [3] 1/2 de vida \n [4] 2/3 de vida "
           "\n [5] 3/4 de vida\n\n")
    while opcion not in resultado:
        opcion = input("Ha ingresado un valor invalido, intentelo nuevamente")
    return resultado[opcion]

def makeCalc(moment, birth, event):
    today = datetime.now()
    birth = (today-birth).days
    event = (today-event).days
    unk = ((birth * moment) - event) / (1-moment)
    print("La fecha final es el ", today+timedelta(days=unk))

date_birth = askDate("Ingrese su fecha de nacimiento en formato DD/MM/YYYY")
date_event = askDate("Ingrese el evento a calcular en formato DD/MM/YYYY")
moment_life = askMoment()
final_result = makeCalc(moment_life, date_birth, date_event)




